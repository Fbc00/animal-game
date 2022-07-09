from .models import Bicho, Aposta
from django.contrib import admin

# Register your models here.

class ApostaAdmin(admin.ModelAdmin):
    list_display = ('bicho', 'data', 'usuario', 'resultado')

class BichoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Aposta, ApostaAdmin)

admin.site.register(Bicho, BichoAdmin)