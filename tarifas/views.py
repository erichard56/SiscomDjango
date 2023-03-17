from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarifa

# Create your views here.

def tarifas(request):
	tarifas = Tarifa.objects.all().order_by('destino', 'dia', 'horaDesde')
	contexto = {'detalles':tarifas}
	return render(request, 'tarifas.html', contexto)