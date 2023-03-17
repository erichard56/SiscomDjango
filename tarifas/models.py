from django.db import models

# Create your models here.

class Tarifa(models.Model):
	DESTINOS = [ 
		('ACAP', 'A Capital'), 
		('AMTE', 'A MonteGrande')
	]
	destino = models.CharField(max_length=4,
		choices = DESTINOS,
		default = 'ACAP')
	DIAS = [
		('0Do', 'Domingo'),
		('1Lu', 'Lunes'),
		('2Ma', 'Martes'),
		('3Mi', 'Miércoles'),
		('4Ju', 'Jueves'),
		('5Vi', 'Viernes'),
		('6Sa', 'Sábado'),
		]
	dia = models.CharField(max_length=3,
		choices = DIAS)
	horaDesde = models.TimeField()
	horaHasta = models.TimeField()

	class Meta():
		ordering = ['destino', 'dia', 'horaDesde', ]

	def __str__(self):
		return f'{self.destino} / {self.dia} / {self.horaDesde} / {self.horaHasta}'