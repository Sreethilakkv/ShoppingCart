from django import forms
from .models import *
from django.forms import fields

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        