from django.contrib import admin

# Register your models here.
from .models import Grupo, Contacto, Grupo_Contacto,CampoExtra, CampoExtra_Grupo, Campo_Contacto



admin.site.register(Grupo)
admin.site.register(Contacto)
admin.site.register(Grupo_Contacto)
admin.site.register(CampoExtra)
admin.site.register(CampoExtra_Grupo)
admin.site.register(Campo_Contacto)