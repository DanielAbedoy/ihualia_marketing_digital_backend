from django.db import models
import json

##Importtacion del Usuario
from marketing.models import Cuenta


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
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE,default='', related_name='contactos')
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
     
    contacto = models.ForeignKey(Contacto, related_name="campos_extra", on_delete=models.CASCADE)
    campo = models.ForeignKey(CampoExtra, on_delete=models.CASCADE)
    valor = models.CharField(max_length=70)
    
    class Meta:
        ordering = ['contacto']

    def __str__(self):
        objeto = {"campo": self.campo.__str__(), "valor": self.valor }
        return (json.dumps(objeto))
