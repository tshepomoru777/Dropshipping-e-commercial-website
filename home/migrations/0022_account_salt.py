# Generated by Django 3.1.4 on 2021-02-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210218_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='salt',
            field=models.CharField(default='hi', max_length=1000),
        ),
    ]
