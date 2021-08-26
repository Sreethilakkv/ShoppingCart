from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

