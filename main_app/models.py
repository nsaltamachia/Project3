from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

# 'add restaurant' post
class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    neighborhood = models.TextField(max_length=150)
    cuisine = models.TextField(max_length=150)
    # foreign key linking user to instance (auth)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# change instance method
def __str__(self):
    return f'{self.name} ({self.id})'