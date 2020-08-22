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


##Modelo del Grupo
class Grupo(models.Model):

    nombre = models.CharField(max_length=150)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.DO_NOTHING , related_name='cuenta_del_grupo', default='')

    class Meta:
        ordering = ['cuenta']

    def __str__(self):
        objeto = {"nombre": self.nombre, "cuenta": self.cuenta}
        return (json.dumps(objeto))        



##Modelo para el Contacto
class Contacto(models.Model):

    nombre = models.CharField(max_length=150)
    correo = models.EmailField(max_length=100)
  
    def __str__(self):
        objeto = {"nombre": self.nombre, "correo": self.correo}
        return json.dumps(objeto)

##Modelo para la relacion entre el grupo y el contacto
class Grupo_Contacto(models.Model):
    contacto = models.ForeignKey(Contacto,on_delete=models.CASCADE,default='', related_name='contacto_grupo')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE,default='', related_name='grupo_contacto')
    class Meta:
        ordering = ['grupo']
    def __str__(self):
        objeto = {"contacto": self.contacto, "grupo": self.grupo}
        return json.dumps(objeto)


class CampoExtra(models.Model):

    nombre = models.CharField(primary_key=True, max_length=100)
    
    def __str__(self):
        return self.nombre

class CampoExtra_Grupo(models.Model):

    clave = models.AutoField(primary_key=True)
    campo_extra = models.ForeignKey(CampoExtra, on_delete=models.CASCADE, related_name='campo_grupo')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='gupo_campo')

    class Meta:
        ordering = ['grupo']

    def __str__(self):
        objeto = {"Campo Extra": self.campo_extra, "Grupo": self.grupo}
        return json.dumps(objeto)


    
class Campo_Contacto(models.Model):
     
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    campo = models.ForeignKey(CampoExtra, on_delete=models.CASCADE)
    valor = models.CharField(max_length=70)
    
    class Meta:
        ordering = ['contacto']

    def __str__(self):
         return '%s - %s - %s' % (self.contacto, self.campo, self.valor)
