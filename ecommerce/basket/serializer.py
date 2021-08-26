from django.db.models.base import Model
from rest_framework import serializers
from .models import Basket

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['id','customer_id','product_id','quantity','created_date','active']
