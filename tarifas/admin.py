from django.contrib import admin
from .models import Tarifa

# Register your models here.

class TarifaAdmin(admin.ModelAdmin):
	list_display = ('destino', 'dia', 'horaDesdeS', 'horaHastaS', )
	list_filter = ('destino', 'dia', )
	ordering = ('destino', 'dia', )

	def horaDesdeS(self, obj:Tarifa) -> str:
		return f"{(obj.horaDesde.strftime('%H:%M'))}"

	def horaHastaS(self, obj:Tarifa) -> str:
		return f"{(obj.horaHasta.strftime('%H:%M'))}"

admin.site.register(Tarifa, TarifaAdmin)




