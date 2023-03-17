from django.shortcuts import render
from .models import Parada

# Create your views here.

def paradas(request):
	paradas = Parada.objects.all().order_by('parv', 'orden', 'nombre')
	contexto = {'detalles':paradas}
	return render(request, 'paradas.html', contexto)