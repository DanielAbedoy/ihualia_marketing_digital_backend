from django.contrib import admin

# Register your models here.
from .models import Grupo, Contacto,CampoExtra, Campo_Contacto



admin.site.register(Grupo)
admin.site.register(Contacto)
admin.site.register(CampoExtra)
admin.site.register(Campo_Contacto)