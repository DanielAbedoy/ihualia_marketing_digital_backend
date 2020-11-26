from django.contrib import admin

from eventos.models import Evento, Asistente_Evento, ImagenPrincipal

# Register your models here.
admin.site.register(Evento)
admin.site.register(Asistente_Evento)
admin.site.register(ImagenPrincipal)

