from django.db import models
import json


#Modelo del Cliente(Empresa)
class Cliente(models.Model):
    
    id_cliente = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=30)
    dominio = models.CharField(max_length=100)
    giro = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id_cliente)


## Modelo del Usuario
class Usuario(models.Model):
    
    
    correo = models.EmailField(max_length=100, unique=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=1500)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30) # Administrador - Colaborador
    estatus = models.CharField(max_length=30)
    imagen = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="usuarios")


    def __str__(self):
        objeto = {"id":str(self.id),"correo": self.correo,"usuario":self.usuario , "nombre": self.nombre, "tipo":self.tipo, "estatus":self.estatus, "imagen":self.imagen, "descripcion": self.descripcion}
        return json.dumps(objeto)


##Modelo de lacuenta
class Cuenta(models.Model):

    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cuentas")
    nombre = models.CharField(max_length=200)
    estatus = models.CharField(max_length=30)

    class Meta:
        ordering = ['id_cliente']

    def __str__(self):
        objeto = {"id":str(self.id),"nombre": self.nombre, "estatus": self.estatus}
        return json.dumps(objeto)


class CuentaUsuario(models.Model):
    
    cuenta = models.ForeignKey(Cuenta, related_name="usuarios", on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name="cuentas",on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        obj = {"cuenta":self.cuenta.__str__(), "usuario":self.usuario.__str__(),"tipo":self.tipo}
        return json.dumps(obj)