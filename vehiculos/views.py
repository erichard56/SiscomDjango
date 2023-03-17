from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehiculo

# Create your views here.

def vehiculos(request):
	vehiculos = Vehiculo.objects.all().order_by('nombre')
	contexto = {'vehiculos':vehiculos}
	return render(request, 'vehiculos.html', contexto)
