from django import forms
from .models import *
from django.forms import fields

class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        