from django.contrib import admin

from encuestas.models import Imagen, Encuesta,Encuestado

# Register your models here.

admin.site.register(Imagen)
admin.site.register(Encuesta)
admin.site.register(Encuestado)
