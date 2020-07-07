from django.db import models
import json

## Modelo del Usuario
class Usuario(models.Model):
    
    correo = models.EmailField(max_length=100, primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=30)
    dominio = models.URLField(max_length=100)
    giro = models.CharField(max_length=150)
    imagen = models.CharField(max_length=100)
    
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        objeto = {"correo": self.correo,"usuario":self.usuario , "nombre": self.nombre}
        return json.dumps(objeto)


##Modelo de lacuenta
class Cuenta(models.Model):

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_de_cuenta")

    class Meta:
        ordering = ['usuario']

    def __str__(self):
        objeto = {"nombre": self.nombre, "tipo": self.tipo}
        return json.dumps(objeto)


