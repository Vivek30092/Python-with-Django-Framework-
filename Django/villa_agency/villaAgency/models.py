from django.db import models

# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobilenumber = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)