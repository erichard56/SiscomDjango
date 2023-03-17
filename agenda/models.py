from django.db import models

# Create your models here.

class Agenda(models.Model):
    fecha = models.DateField()
    destino = 