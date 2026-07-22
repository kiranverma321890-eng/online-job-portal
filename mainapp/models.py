from django.db import models

# Create your models here.

class LoginInfo(models.Model):
    usertype = models.CharField(max_length=15)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=256)