from django.db import models

# Create your models here.

class Vehiculo(models.Model):
	nombre = models.CharField(max_length=50)
	asientos = models.IntegerField()
	ESTADOS = [
		('OK', 'Disponible'),
		('FS', 'Fuera de Servicio'),
	]
	estado = models.CharField(max_length=2,
		choices = ESTADOS,
		default = 'OK')

	def __str__(self):
		return f'{self.nombre} / {self.asientos}'
