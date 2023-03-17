from django.contrib import admin
from .models import Feriado

# Register your models here.
class FeriadoAdmin(admin.ModelAdmin):
	list_display = ('fecha', )
	list_filter = ('fecha', )

admin.site.register(Feriado, FeriadoAdmin)