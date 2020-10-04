from django.db import models

from contacto.models import Grupo, Contacto
from marketing.models import Cuenta

class Boletin (models.Model):

  id_cuenta = models.ForeignKey(Cuenta, related_name="boletin_cuenta", on_delete=models.CASCADE)
  asunto = models.CharField(max_length=500)
  tipo_publicacion = models.CharField(max_length=20)
  contenido = models.TextField()
  estatus = models.CharField(max_length=30)
  fecha_creado = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.asunto + " - " + self.tipo_publicacion + " - "


class EnvioBoletin(models.Model):

  id_boletin = models.ForeignKey(Boletin, related_name="envio_boletin", on_delete=models.CASCADE)
  ids_contactos = models.TextField()
  ids_grupos = models.TextField()

  def __str__(self):
    return str(self.id_boletin) + " - " + self.ids_contactos


class FechaHoraPublicacionBoletin(models.Model):
  
  id_boletin = models.ForeignKey(Boletin,related_name="fecha_boletin",on_delete=models.CASCADE)
  fecha = models.CharField(max_length=20)
  hora = models.CharField(max_length=10)
  ids_grupos = models.TextField()

  def __str__(self):
    return str(self.id_boletin) + " - " + self.fecha


class GrupoEnvioBoletin(models.Model):

  id_boletin = models.ForeignKey(Boletin, related_name="boletin_grupo", on_delete=models.CASCADE)
  id_grupo = models.ForeignKey(Grupo, related_name="grupo_boletin", on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id_boletin) + " - " + str(self.id_grupo)


class PlantillaBoletin(models.Model):

  contenido = models.TextField()
  categoria = models.CharField(max_length=100)

  def __str__(self):
    return "Plantilla: " 


class ImagenBoletin(models.Model):

  nombre = models.CharField(max_length=200)
  cuenta = models.CharField(max_length=10)

  def __str__(self):
    return self.nombre


class LinkBoletin(models.Model):

  id_boletin = models.ForeignKey(Boletin, related_name="link_boletin",on_delete=models.CASCADE)
  link = models.CharField(max_length=1000)

  def __str__(self):
    return self.link


class SeenContactoBoletin(models.Model):
  id_boletin = models.ForeignKey(Boletin, related_name="boletin_seen", on_delete=models.CASCADE)
  id_contacto = models.ForeignKey(Contacto, related_name="contacto_seen", on_delete=models.CASCADE)
  fecha_visto = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.id_boletin) + " - " + str(self.id_contacto)


class SeenLinkBoletin(models.Model):
  id_link = models.ForeignKey(LinkBoletin, related_name="link_seen", on_delete=models.CASCADE)
  id_contacto = models.ForeignKey(Contacto, related_name="contactolink_seen", on_delete=models.CASCADE)
  fecha_visto = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.id_link) + " - " + str(self.id_contacto)

  




