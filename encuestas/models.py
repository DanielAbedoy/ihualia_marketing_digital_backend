from django.db import models

# Create your models here.

from contacto.models import Cuenta

class Imagen(models.Model):

  encuesta = models.CharField(max_length=10)
  nombre = models.CharField(max_length=200)

class Encuesta(models.Model):

  nombre = models.CharField(max_length=35)
  presentacion = models.CharField(max_length=1000)
  instrucciones = models.CharField(max_length=1000)
  imagen = models.CharField(max_length=10, blank=True)
  anonima = models.BooleanField(null=True)
  ponderacion = models.BooleanField(null=True)
  paginacion = models.CharField(max_length=10, blank=True)
  preguntas_json = models.TextField(blank=True)
  despedida = models.CharField(max_length=1000, blank=True)
  estatus = models.CharField(max_length=20)
  url = models.CharField(max_length=100, blank=True)
  cuenta = models.ForeignKey(Cuenta, related_name="encuestas", on_delete=models.CASCADE)

class Encuestado(models.Model):

  encuesta = models.ForeignKey(Encuesta, related_name="encuestados", on_delete=models.CASCADE)
  nombre = models.CharField(max_length=100, blank=True)
  correo = models.CharField(max_length=100, blank=True)
  respuestas_json = models.TextField()
  creado = models.DateField(auto_now_add=True)
  