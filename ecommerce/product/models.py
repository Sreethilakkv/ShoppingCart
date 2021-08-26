from django.db import models


# Create your models here.
class Product(models.Model):
     product_name = models.CharField(max_length=100)
     product_id = models.IntegerField(primary_key=True)
     description = models.CharField(max_length=100)
     price = models.IntegerField(null=False)
     created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
