# Generated by Django 3.0.11 on 2021-01-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/', blank=True, null=True),  # Added 'upload_to' for better file management
        ),
    ]
