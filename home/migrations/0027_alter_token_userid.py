# Generated by Django 4.2.16 on 2024-10-16 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_account_id_alter_account_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]