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
    
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name="usuarios")
    correo = models.EmailField(max_length=100, primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30) # Administrador - Colaborador
    estatus = models.CharField(max_length=30)
    imagen = models.CharField(max_length=100)


    def __str__(self):
        objeto = {"correo": self.correo,"usuario":self.usuario , "nombre": self.nombre, "tipo":self.tipo, "estatus":self.estatus, "imagen":self.imagen}
        return json.dumps(objeto)


##Modelo de lacuenta
class Cuenta(models.Model):

    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cuentas")
    nombre = models.CharField(max_length=200)
    estatus = models.CharField(max_length=30)

    class Meta:
        ordering = ['id_cliente']

    def __str__(self):
        objeto = {"nombre": self.nombre, "estatus":self.estatus}
        return json.dumps(objeto)


class CuentaUsuario(models.Model):
    
    cuenta = models.ForeignKey(Cuenta, related_name="usuarios", on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name="cuentas",on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo
        

