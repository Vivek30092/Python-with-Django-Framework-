from django.db import models

# Create your models here.
class student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=30)
    sfees = models.IntegerField()
    saddr = models.CharField(max_length=30)
    sunm =models.CharField(max_length=30)
    pw = models.CharField(max_length=30)