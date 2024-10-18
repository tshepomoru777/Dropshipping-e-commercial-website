from django.contrib import admin
from .models import Account, Token, Order, ContactMessage  # Import relevant models from home

# Register your models here.
admin.site.register(Account)
admin.site.register(Token)
admin.site.register(Order)
admin.site.register(ContactMessage)  # Include ContactMessage here
