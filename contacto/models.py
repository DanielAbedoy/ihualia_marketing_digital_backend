from django.db import models
import json

##Importtacion del Usuario
from marketing.models import Cuenta



class CampoExtra(models.Model):

    nombre = models.CharField(primary_key=True, max_length=100)
    
    def __str__(self):
        return self.nombre

    
##Modelo del Grupo
class Grupo(models.Model):

    nombre = models.CharField(max_length=150)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE , related_name='grupos', default='')
    campos_extra = models.ManyToManyField(CampoExtra,related_name="grupos", blank=True)

    def __str__(self):
        objeto = {"nombre": self.nombre}
        return (json.dumps(objeto))        



##Modelo para el Contacto
class Contacto(models.Model):

    nombre = models.CharField(max_length=150)
    correo = models.EmailField(max_length=100)
    grupo = models.ForeignKey(Grupo, related_name="contactos", on_delete=models.CASCADE)

    def __str__(self):
        objeto = {"nombre": self.nombre, "correo": self.correo}
        return json.dumps(objeto)


class Campo_Contacto(models.Model):
     
    contacto = models.ForeignKey(Contacto, related_name="campos_extra", on_delete=models.CASCADE)
    campo = models.ForeignKey(CampoExtra, on_delete=models.CASCADE)
    valor = models.CharField(max_length=1000)
    
    class Meta:
        ordering = ['contacto']

    def __str__(self):
        objeto = {"campo": self.campo.__str__(), "valor": self.valor }
        return (json.dumps(objeto))
