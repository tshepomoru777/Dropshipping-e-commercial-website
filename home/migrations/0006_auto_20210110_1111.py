# Generated by Django 3.0.11 on 2021-01-10 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',  # Singular name 'Category'
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField(default='default-slug', unique=True)),  # Updated default slug
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),  # Updated default slug for Product
        ),
        migrations.DeleteModel(
            name='Categories',  # Deleting the old Categories model
        ),
        migrations.AddField(
            model_name='product',
            name='category',  # Linking to the new Category model
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Category'),
        ),
    ]
