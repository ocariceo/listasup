from django import forms
from django.forms import ModelForm

from .models import *


class CompraForm(forms.ModelForm):
	producto= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Agregar un nuevo producto'}))

	class Meta:
		model = Compra
		fields = '__all__'