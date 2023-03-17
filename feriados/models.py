from django.db import models

# Create your models here.

class Feriado(models.Model):
	fecha = models.DateField()

	def __str__(self):
		return (self.fecha.strftime('%Y-%m-%d'))
