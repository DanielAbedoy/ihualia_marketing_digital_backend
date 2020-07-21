from django.contrib import admin

from .models import Usuario, Cuenta, Cliente, Usuario_Cuenta

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Cliente)
admin.site.register(Usuario_Cuenta)
