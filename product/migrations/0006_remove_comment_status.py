# Generated by Django 3.0.11 on 2021-01-10 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210110_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
    ]