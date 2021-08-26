from django.urls import path
from .views import  *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    path('',product_list,name="product_list"),
    path('product_delete/<int:pk>/',product_delete,name="product_delete"),
    path('product_edit/<int:pk>/', product_edit,name="product_edit"),  
    path('product_update/<int:pk>/', product_update,name="product_update"),  
    path('product_detail/<int:pk>/',product_details,name="product_details"),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)