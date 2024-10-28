from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.test import APITestCase  # Importing APITestCase
from .serializers import ProductSerializer, CommentSerializer
from .models import Product, Comment

# Existing index view
def index(request):
    return HttpResponse("This is the product index page.")

# New add_comment view
@api_view(['POST'])
def add_comment(request, p_id):
    try:
        product = Product.objects.get(id=p_id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(product=product, users=request.user)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Your existing test cases
class ProductSerializerTest(APITestCase):
    def test_product_serializer(self):
        product_data = {
            'title': 'Sample Product',
            'description': 'This is a test product.',
            'price': '10.99',
            'category': 1,  # Assuming category with id=1 exists
            'image': 'http://example.com/image.jpg'
        }
        serializer = ProductSerializer(data=product_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['title'], 'Sample Product')

class CommentSerializerTest(APITestCase):
    def test_comment_serializer(self):
        comment_data = {
            'subject': 'Great Product!',
            'comment': 'I really liked this product.',
            'rate': 5,
            'product': 1,  # Assuming product with id=1 exists
            'users': 1,    # Assuming user with id=1 exists
        }
        serializer = CommentSerializer(data=comment_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['subject'], 'Great Product!')