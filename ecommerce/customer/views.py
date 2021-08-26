from customer.form import Customerform
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse, response
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializer import CustomerSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response, responses
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def customer_list(request):
    cust=Customerform(request.POST, request.FILES)
    if request.method == 'GET':
        if cust.is_valid():
            cust.save()

        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        # return Response(serializer.data)
        context = {'cust':cust, 'customers':customers}
        return render(request, 'customers.html', context)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            customers = Customer.objects.all()
            return render(request, 'customers.html', {'cust':cust, 'customers':customers})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def customer_details(request,pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def customer_delete(request,pk):
    try:
        product = Customer.objects.get(pk=pk)

    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    prod=Customerform(request.POST, request.FILES)
    products = Customer.objects.all()
    return redirect("/customer/")  