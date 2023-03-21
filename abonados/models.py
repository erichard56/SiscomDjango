from django.db import models
from paradas.models import Parada
from siscom.choices import DESTINOS, DIAS

# Create your models here.

class Abonado(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=30)
	observaciones = models.CharField(max_length=200)
	numeroAbonado = models.IntegerField()
	documento = models.CharField(max_length=45)
	localidad = models.CharField(max_length=45)
	codigoPostal = models.CharField(max_length=10)

	def __str__(self):
		return f'{self.nombre} / {self.numeroAbonado}'

class Abono(models.Model):
	idAbonado = models.ForeignKey(Abonado, on_delete=models.CASCADE)
	fechaDesde = models.DateField()
	fechaHasta = models.DateField()

	def __str__(self):
		return f'{self.idAbonado} / {self.fechaDesde.strftime("%Y-%m-%d")} / {self.fechaHasta.strftime("%Y-%m-%d")}'

class AbonadoDia(models.Model):
	idAbonado = models.ForeignKey(Abonado, on_delete=models.CASCADE)
	destino = models.CharField(max_length=4,
		choices = DESTINOS, default = 'ACAP')
	dia = models.CharField(max_length=3, choices = DIAS)
	hora = models.TimeField()
	idparada = models.ForeignKey(Parada, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.idAbonado} / {self.destino} / {self.dia} / {self.hora}'
