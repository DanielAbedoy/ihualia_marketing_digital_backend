from django.contrib import admin

#Models
from marketing_digital.models import (
  Cliente, Usuario, Cuenta, Usuario_Cuenta,
  Grupo, Contacto, Grupo_Contacto, CampoExtra, Campo_Contacto, CampoExtra_Grupo,
)

admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Usuario_Cuenta)
admin.site.register(Grupo)
admin.site.register(Contacto)
admin.site.register(Grupo_Contacto)
admin.site.register(CampoExtra)
admin.site.register(Campo_Contacto)
admin.site.register(CampoExtra_Grupo)
