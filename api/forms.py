from django import forms
from .models import *
  
class imageForm(forms.ModelForm):
    image = forms.ImageField()
  
    class Meta:
        model = image
        fields = ['image']