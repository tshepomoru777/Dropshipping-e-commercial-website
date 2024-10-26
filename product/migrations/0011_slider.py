# Generated by Django 3.0.11 on 2021-01-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('subtitle', models.CharField(blank=True, max_length=50)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]