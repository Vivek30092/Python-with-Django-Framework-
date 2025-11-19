from django.db import models

# Create your models here.
class Registration(models.Model):
    emid = models.IntegerField()
    ename = models.CharField(max_length=30)
    desg = models.CharField(max_length=50)
    loc = models.CharField(max_length=30)
    salary = models.IntegerField()
    exp = models.IntegerField()
    status = models.IntegerField()
    # eid = models.IntegerField()
    # ename = models.CharField(max_length=30)
    # esal = models.IntegerField()
    # eaddr = models.CharField(max_length=30)
    # eunm = models.CharField(max_length=30)
    # pw = models.CharField(max_length=30)