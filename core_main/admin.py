from .models import Bicho, Aposta, Sorteio
from django.contrib import admin

# Register your models here.

class ApostaAdmin(admin.ModelAdmin):
    list_display = ('bicho', 'data', 'usuario', 'resultado', 'valor', 'ganho',)

class BichoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'grupo',)

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('data_sorteio', 'bicho_sorteado', 'data_criacao')

admin.site.register(Aposta, ApostaAdmin)
admin.site.register(Sorteio, SorteioAdmin)
admin.site.register(Bicho, BichoAdmin)