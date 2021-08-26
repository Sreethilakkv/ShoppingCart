from product.form import Productform
from django.shortcuts import render,redirect  
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Product
from .serializer import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response, responses
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET','POST'])
def product_list(request):
    prod=Productform(request.POST, request.FILES)
    if request.method == 'GET':
        if prod.is_valid():
            prod.save()

        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        #return Response(serializer.data)
        context = {'prod':prod, 'products':products}
        return render(request, 'product.html', context)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            products = Product.objects.all()
            return render(request, 'product.html', {'prod':prod, 'products':products})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def product_details(request,pk):
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def product_delete(request,pk):
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    prod=Productform(request.POST, request.FILES)
    products = Product.objects.all()
    return redirect("/product/")  

def product_edit(request, pk):  
    product = Product.objects.get(pk=pk)
    return render(request,'edit_product.html', {'product':product})  

def product_update(request, pk):
    product = Product.objects.get(pk=pk)  
    print(request.POST)
    form = Productform(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/product/")  
    # return render(request, 'edit_product.html', {'product': product})  
    return redirect("/product/")





    # try:
    #     product = Product.objects.get(pk=pk)

    # except Product.DoesNotExist:
    #     return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    # serializer = ProductSerializer(product,data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     render(request,'product.html', {'product':product})
    # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)