from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import UserLoginView, RegisterView, CheckoutView

urlpatterns = [
    # Frontend URLs
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('account/', views.account, name="account"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('aboutus/', views.about_us, name="about_us"),
    path('contactus/', views.contact_us, name="contact"),
    path('service/', views.service, name="service"),
    path('faq/', views.faq, name="faq"),
    path('policy/', views.policy, name="policy"),
    path('shop/', views.product_list, name="product_list"),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
    path('login/', views.login, name="login"),

    # API URLs
    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/login/', UserLoginView.as_view(), name="login"),  # More consistent name for login API
    path('api/checkout/', CheckoutView.as_view(), name="checkout"),  # Clearer naming for checkout with token requirement

    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Future feature (uncomment if needed)
    # path('category/<int:id>/<slug:slug>/', views.category_product, name="category_product"),
]
