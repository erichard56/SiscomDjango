from django.shortcuts import render
from django.http import HttpResponse
from .models import Horario

# Create your views here.

def horarios(request):
	horarios = Horario.objects.all().distinct().order_by('destino', 'dia', 'hora')
	contexto = {'detalles':horarios}
	return render(request, 'horarios.html', contexto)