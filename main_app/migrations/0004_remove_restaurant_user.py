# Generated by Django 4.2.7 on 2023-11-23 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_restaurant_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='user',
        ),
    ]