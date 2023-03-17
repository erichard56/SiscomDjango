from django.contrib import admin
from .models import Vehiculo

# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'asientos', 'estado')
	list_filter = ('estado', 'asientos', )
	search_fields = ('nombre', )

admin.site.register(Vehiculo, VehiculoAdmin)
