from django.contrib import admin

from .models import Usuario, Cuenta, Cliente, CuentaUsuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Cliente)
admin.site.register(CuentaUsuario)