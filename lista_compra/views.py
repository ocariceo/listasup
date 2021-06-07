from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
	compras = Compra.objects.all()

	form = CompraForm()

	if request.method =='POST':
		form = CompraForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'compras':compras, 'form':form}
	return render(request, 'lista_compra/lista.html', context)

def actualizarCompra(request, pk):
	compra = Compra.objects.get(id=pk)

	form = CompraForm(instance=compra)

	if request.method == 'POST':
		form = CompraForm(request.POST, instance=compra)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'lista_compra/actualizar_compra.html', context)

def borrarCompra(request, pk):
	item = Compra.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'lista_compra/borrar_compra.html', context)

