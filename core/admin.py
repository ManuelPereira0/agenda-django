from django.contrib import admin
from core.models import Evento

# Register your models here.

#No Admin retorna os campos solicitados
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    
    #Acrescenta um filter pelo(s), campos da tabela do db
    # list_filter = ('titulo', 'usuario')
    
    
admin.site.register(Evento, EventoAdmin)