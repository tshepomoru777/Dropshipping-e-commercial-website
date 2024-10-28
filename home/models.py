from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# User model manager

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Securely hash and store the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

# User model
class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)  # Reduced length
    email = models.EmailField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Removed the salt field for security and simplicity reasons
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def tokens(self):
        # Placeholder for token generation logic
        return ''

# Token model
class Token(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    token = models.CharField(max_length=500)  # Reduced max_length, tokens are generally not this large
    created_at = models.DateTimeField(auto_now_add=True)

# Order model
class Order(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Phone number, potentially with validation later
    email = models.EmailField(max_length=255)
    note = models.CharField(blank=True, max_length=1000)  # Reduced length for 'note'
    address_op = models.CharField(blank=True, max_length=500)
    company = models.CharField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
# Contact message model
class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    note = models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Contact form model
class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'email', 'message']