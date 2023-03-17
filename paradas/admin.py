from django.contrib import admin
from .models import Parada

# Register your models here.

class ParadaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'orden', 'parv')
	list_filter = ('parv', )

admin.site.register(Parada, ParadaAdmin)
