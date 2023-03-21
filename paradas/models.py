from django.db import models
from siscom.choices import DESTINOS, DIAS, PARADAS

# Create your models here.

class Parada(models.Model):
	nombre = models.CharField(max_length=50)
	orden = models.IntegerField()
	parv = models.IntegerField(choices = PARADAS, default = 0)

	def __str__(self):
		return f'{self.parv} / {self.orden} / {self.nombre}'