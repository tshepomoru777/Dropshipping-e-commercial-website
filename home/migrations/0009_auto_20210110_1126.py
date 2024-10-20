# Generated by Django 3.0.11 on 2021-01-10 04:26

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210110_1121'),
    ]

    operations = [
        # Keep the category relationship in the Product model
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
        ),
        
        # Keep the slug field in Product for unique URL slugs
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
        
        # Keep the variant field to manage product variations
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], default='None', max_length=10),
        ),

        # Adding image field to Category model
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),

        # Ensure unique slugs in the Category model
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        
        # Adjust Product name field
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
