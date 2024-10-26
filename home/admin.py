from django.contrib import admin
from .models import Account, Token, Order, ContactMessage

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_verified')  # Add relevant fields
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_verified')

class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at')
    search_fields = ('user__username', 'token')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('created_at',)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

# Register your models with their respective admin classes
admin.site.register(Account, AccountAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
