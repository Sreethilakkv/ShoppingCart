from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.
class Basket(models.Model):
     id = models.IntegerField(primary_key=True)
     customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
     product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity = models.IntegerField(null=False)
     created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
     active = models.BooleanField(default=True)