from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AccountRegisterSerializer, OrderSerializer
from .models import *
from product.models import *
from django.utils.crypto import get_random_string

# Utility function to get common context
def get_common_context():
    return {'category': Category.objects.all()}

def home(request):
    context = get_common_context()
    context.update({
        'sliders': Slider.objects.all(),
        'latest': Product.objects.all().order_by('-id')[:16],
    })
    return render(request, 'pages/home.html', context)

def cart(request):
    context = get_common_context()
    return render(request, 'pages/cart.html', context)

def checkout(request):
    context = get_common_context()
    return render(request, 'pages/checkout.html', context)

def account(request):
    context = get_common_context()
    return render(request, 'pages/account.html', context)

def wishlist(request):
    context = get_common_context()
    return render(request, 'pages/wish_list.html', context)

def about_us(request):
    context = get_common_context()
    return render(request, 'pages/about_us.html', context)

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.ip = request.META.get('REMOTE_ADDR')
            contact_message.save()
            messages.success(request, "Your message has been sent. Thanks for contacting us!")
            return HttpResponseRedirect('/contactus')
    else:
        form = ContactForm()

    context = get_common_context()
    context.update({'form': form})
    return render(request, 'pages/contact_us.html', context)

def service(request):
    context = get_common_context()
    return render(request, 'pages/service.html', context)

def faq(request):
    context = get_common_context()
    return render(request, 'pages/faq.html', context)

def policy(request):
    context = get_common_context()
    return render(request, 'pages/policy.html', context)

def product_list(request):
    context = get_common_context()
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context.update({'page_obj': page_obj})
    return render(request, 'pages/product_list.html', context)

def product_detail(request, id, slug):
    context = get_common_context()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id).order_by('-id')
    context.update({
        'product': product,
        'images': images,
        'comments': comments,
    })
    return render(request, 'pages/product_detail.html', context)

def login_view(request):
    context = get_common_context()
    return render(request, 'pages/login.html', context)

class RegisterView(generics.GenericAPIView):
    serializer_class = AccountRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()

        # Use Django's set_password() to securely hash the password
        account.set_password(user['password'])
        account.save()

        # Generate JWT token for the registered user
        refresh = RefreshToken.for_user(account)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        account = authenticate(email=email, password=password)

        if account is not None:
            refresh = RefreshToken.for_user(account)
            return Response({
                'email': account.email,
                'username': account.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

class CheckoutView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request):
        token = request.data.get('token')
        if token and self.token_is_valid(token):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid or missing token'}, status=status.HTTP_400_BAD_REQUEST)

    def token_is_valid(self, token):
        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False