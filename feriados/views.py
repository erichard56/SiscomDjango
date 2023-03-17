from django.shortcuts import render
from django.http import HttpResponse
from .models import Feriado

# Create your views here.

def feriados(request):
	feriados = Feriado.objects.all().order_by('fecha')
	print(feriados[0])
	contexto = {'detalles':feriados}
	return render(request, 'feriados.html', contexto)