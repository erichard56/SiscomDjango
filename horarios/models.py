from django.db import models
from siscom.choices import DESTINOS, DIAS

# Create your models here.

class Horario(models.Model):
	destino = models.CharField(max_length=4,
		choices = DESTINOS, default = 'ACAP')
	dia = models.CharField(max_length=3, choices = DIAS)
	hora = models.TimeField()

	class Meta():
		ordering = ['destino', 'dia', 'hora', ]

	def __str__(self):
		return f"{self.destino} / {self.dia} / {self.hora.strftime('%H:%M')}"