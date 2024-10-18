from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# User model manager

class AccountManager(BaseUserManager):
    def create_user(self, email, salt, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, salt=salt, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  # Use the specified database
        return user

    
    def create_superuser(self, email, salt, password=None, **extra_fields):
    
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, salt, password, **extra_fields)

# User model
class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=300, unique=True)
    email = models.EmailField(max_length=300, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    salt = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'salt']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''

# Token model
class Token(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)  # Use direct reference to Account
    token = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

# Order model
class Order(models.Model):
    first_name = models.CharField(max_length=5000)
    last_name = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    city = models.CharField(max_length=5000)
    district = models.CharField(max_length=5000)
    phone = models.CharField(max_length=15)  # Change to CharField for better phone number handling
    email = models.EmailField(max_length=5000)
    note = models.CharField(blank=True, max_length=10000)
    address_op = models.CharField(blank=True, max_length=5000)
    company = models.CharField(blank=True, max_length=5000)

# Contact message model
class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)  # No max_length for TextField
    ip = models.GenericIPAddressField(blank=True, null=True)  # Use GenericIPAddressField for IP
    note = models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Contact form model
class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'email', 'message']  # Use list for fields instead of set
