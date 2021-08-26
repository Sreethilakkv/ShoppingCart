import datetime
from product.models import Product
from customer.models import Customer
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse, response
from rest_framework.parsers import JSONParser
from .models import Basket
from .serializer import BasketSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response, responses
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def basket_list(request):
    if request.method == 'GET':
        basket = Basket.objects.all()
        serializer = BasketSerializer(basket,many=True)
        return render(request, 'basket.html', {'basket':basket})
    elif request.method == 'POST':
        serializer = BasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def basket_details(request,pk):
    try:
        basket = Basket.objects.get(pk=pk)
    except Basket.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BasketSerializer(basket)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BasketSerializer(basket,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        basket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def addTo_basket(request,pk):
    customer = Customer.objects.get(pk=1)
    product = Product.objects.get(pk=pk)
    basket = Basket()
    basket.customer_id=customer
    basket.product_id=product
    basket.created_date=datetime.datetime.now()
    basket.quantity=1
    basket.save()
    return redirect("home")  

def basket_delete(request,pk):
    try:
        basket = Basket.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    basket.delete()
    basket = Basket.objects.all()
    return redirect("/basket/") 
    # return render(request, 'basket.html', {'basket':basket})  
