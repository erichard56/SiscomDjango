from django.contrib import admin
from .models import Abonado, Abono, AbonadoDia

# Register your models here.

class AbonadoAdmin(admin.ModelAdmin):
	list_display = ('nombre','direccion', )
	list_filter = ('nombre', )

admin.site.register(Abonado, AbonadoAdmin)

class AbonoAdmin(admin.ModelAdmin):
	list_display = ('idAbonado', )
	list_filter = ('fechaDesde', 'fechaHasta', )

admin.site.register(Abono, AbonoAdmin)

class AbonadoDiaAdmin(admin.ModelAdmin):
	list_display = ('idAbonado', )
	list_filter = ('idAbonado', 'destino', 'dia', )

admin.site.register(AbonadoDia, AbonadoDiaAdmin)