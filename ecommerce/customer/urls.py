from django.urls import path
from .views import  customer_details, customer_list, customer_delete
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customer'

urlpatterns = [
    path('',customer_list,name="customer_list"),
    path('customer_delete/<int:pk>/',customer_delete,name="customer_delete"),
    path('customer_detail/<int:pk>/',customer_details,name="customer_details"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)