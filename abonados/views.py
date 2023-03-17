from django.shortcuts import render
from django.http import HttpResponse
from .models import Abonado, Abono, AbonadoDia

# Create your views here.

def abonados(request):
	abonados = Abonado.objects.all().order_by('nombre')
	contexto = {'abonados':abonados}
	return render(request, 'abonados.html', contexto)

def detalles(request, id):
	abonados = Abonado.objects.all().filter(id=id)
	abonos = Abono.objects.all().filter(idAbonado=id).order_by('fechaDesde')
	abonadodias = AbonadoDia.objects.all().filter(idAbonado=id).order_by('destino', 'dia', 'hora')
	contexto = {'detalles':[abonados, abonos, abonadodias]}
	return render(request, 'detalles.html', contexto)