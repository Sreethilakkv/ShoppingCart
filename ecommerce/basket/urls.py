from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'basket'

urlpatterns = [
    path('',basket_list,name="basket_list"),
    path('addTo_basket/<int:pk>/',addTo_basket),
    path('basketdetail/<int:pk>/',basket_details),
    path('basket_delete/<int:pk>/',basket_delete),
]