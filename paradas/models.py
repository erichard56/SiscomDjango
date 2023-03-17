from django.db import models

# Create your models here.

class Parada(models.Model):
	nombre = models.CharField(max_length=50)
	orden = models.IntegerField()
	PARADAS = [
		(0, 'A Capital'),
		(1, 'A Monte Grande'),
		(2, 'Ambos'),
	]
	parv = models.IntegerField(
		choices = PARADAS,
		default = 0)

	def __str__(self):
		return f'{self.parv} / {self.orden} / {self.nombre}'