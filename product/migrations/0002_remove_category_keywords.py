# Generated by Django 3.0.11 on 2021-01-10 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='keywords',
        ),
    ]