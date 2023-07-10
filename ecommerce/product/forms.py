from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UniversityForm(forms.Form):
  name=forms.CharField(max_length=105, widget=forms.TextInput(attrs={'autofocus': True}),)
  # name=forms.CharField(max_length=105, widget=forms.TextInput(attrs={'autofocus': True}),blank=True)
  # (label='Product name')
  
  # date_of_birth=forms.DateField()

class UniversityForm1(forms.Form):
  # name=forms.CharField(label='Product name')
  # date_of_birth=forms.DateField()
  # eid=forms.CharField(label='Product id:')
  eid=forms.CharField(label='Product id:')
  ename=forms.CharField(label='Product Name:')

 
