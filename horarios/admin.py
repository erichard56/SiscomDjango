from django.contrib import admin
from .models import Horario

# Register your models here.

class HorarioAdmin(admin.ModelAdmin):
	list_display = ('destino', 'dia', 'horaS', )
	list_filter = ('destino', 'dia', )

	def horaS(self, obj:Horario) -> str:
		return f"{(obj.hora.strftime('%H:%M'))}"

admin.site.register(Horario, HorarioAdmin)
