from django.db import models
from siscom.choices import DESTINOS, DIAS, PARADAS

# Create your models here.

class Tarifa(models.Model):
	destino = models.CharField(max_length=4,
		choices = DESTINOS, default = 'ACAP')
	dia = models.CharField(max_length=3, choices = DIAS)
	horaDesde = models.TimeField()
	horaHasta = models.TimeField()

	class Meta():
		ordering = ['destino', 'dia', 'horaDesde', ]

	def __str__(self):
		return f'{self.destino} / {self.dia} / {self.horaDesde} / {self.horaHasta}'