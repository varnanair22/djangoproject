from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    pswd = models.CharField(max_length= 100)
    type = models.CharField(max_length = 50)

class Currency_Details(models.Model):
    curr1 = models.CharField(max_length=100)
    curr2 = models.CharField(max_length= 100)
    conversion_rate = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)
