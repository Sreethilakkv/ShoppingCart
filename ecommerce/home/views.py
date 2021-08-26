from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response, responses
from product.models import Product

# Create your views here.

@api_view(['GET','POST'])
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})