from django.db import models
import json

from contacto.models import Grupo, Contacto
from marketing.models import Cuenta

class Boletin (models.Model):

  id_cuenta = models.ForeignKey(Cuenta, related_name="boletin_cuenta", on_delete=models.CASCADE)
  asunto = models.CharField(max_length=500)
  publicacion = models.CharField(max_length=500)
  contenido = models.TextField(blank=True)
  estatus = models.CharField(max_length=30, blank=True)
  fecha_creado = models.DateField(auto_now=True)

  grupos = models.ManyToManyField(Grupo, related_name="boletines", blank=True)
  links = models.TextField(blank=True)
  enviados= models.TextField(blank=True)

  def __str__(self):
    return str(self.id)


class ImagenBoletin(models.Model):

  nombre = models.CharField(max_length=200)
  cuenta = models.CharField(max_length=10)

  def __str__(self):
    return self.nombre


class SeenContactoBoletin(models.Model):
  id_boletin = models.ForeignKey(Boletin, related_name="contactos_vistos", on_delete=models.CASCADE)
  id_contacto = models.ForeignKey(Contacto, related_name="contacto_seen", on_delete=models.CASCADE)
  fecha_visto = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    objeto ={"contacto": self.id_contacto.__str__(), "fecha": self.fecha_visto.__str__() }
    return json.dumps(objeto)


class SeenLinkBoletin(models.Model):
  boletin = models.ForeignKey(Boletin, related_name="links_vistos", on_delete=models.CASCADE)
  id_link = models.CharField(max_length=10)
  id_contacto = models.ForeignKey(Contacto, related_name="contactolink_seen", on_delete=models.CASCADE)
  fecha_visto = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    objeto = {"contacto": self.id_contacto.__str__(), "fecha":self.fecha_visto.__str__()}
    return json.dumps(objeto)

  




