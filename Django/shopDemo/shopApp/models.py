from django.db import models

# Create your models here.
class Customers(models.Model):
    cname = models.CharField(max_length=50)
    cadd = models.CharField(max_length=90)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    unm = models.CharField(max_length=70)
    pw = models.CharField(max_length=70)