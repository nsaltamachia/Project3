from django.db import models
# import user for auth
from django.contrib.auth.models import User


# Create your models here.
class Restaurant(models.Model):
    # foreign key linking user to instance (auth)
    user = models.ForeignKey(User, on_delete=models.CASCADE)