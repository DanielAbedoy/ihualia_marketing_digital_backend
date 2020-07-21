from django.db import models
import json


#Modelo del Cliente(Empresa)
class Cliente(models.Model):
    
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=30)
    dominio = models.CharField(max_length=100)
    giro = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre + " - " + self.razon_social + " - " + self.dominio


## Modelo del Usuario
class Usuario(models.Model):
    
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name="cliente_usuario")
    correo = models.EmailField(max_length=100, primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30) # Administrador - Colaborador
    estatus = models.CharField(max_length=30)
    imagen = models.CharField(max_length=100)

    def __str__(self):
        objeto = {"correo": self.correo,"usuario":self.usuario , "nombre": self.nombre}
        return json.dumps(objeto)


##Modelo de lacuenta
class Cuenta(models.Model):

    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cuenta_de_cliente")
    nombre = models.CharField(max_length=200)
    estatus = models.CharField(max_length=30)

    class Meta:
        ordering = ['id_cliente']

    def __str__(self):
        objeto = {"nombre": self.nombre, "estatus":self.estatus}
        return json.dumps(objeto)


class Usuario_Cuenta(models.Model):

    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="id_usuario")
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name="id_cuenta")
    tipo = models.CharField(max_length=30)  # Responsable - Apoyo

    def __str__(self):
        return self.id_usuario + " - " + self.id_cuenta + " - " + self.tipo