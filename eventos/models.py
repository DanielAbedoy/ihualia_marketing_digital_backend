from django.db import models
import json

from marketing.models import Cuenta

class Evento(models.Model):

  id_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE, related_name="evento_cuenta")
  nombre = models.CharField(max_length=200)
  tipo = models.CharField(max_length=100)
  categoria = models.CharField(max_length=70)
  sub_categoria = models.CharField(max_length=70)
  ubicacion = models.TextField(blank=True)
  fecha_hora_inicio = models.DateTimeField(null=True)
  fecha_hora_fin = models.DateTimeField(null=True)
  zona_horaria = models.CharField(max_length=100, blank=True)
  resumen = models.CharField(max_length=1000, blank=True)
  estatus = models.CharField(max_length=50)
  imagen = models.CharField(max_length=10, blank=True)
  url = models.CharField(max_length=200, blank=True)

  etiquetas = models.CharField(max_length=1000, blank=True)
  componentes = models.TextField(blank=True)
  boletos = models.TextField(blank=True)


  def __str__(self):
    return str(self.id_cuenta) + " - " + self.nombre

class ImagenPrincipal(models.Model):
  evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="imegenes")
  name = models.CharField(max_length=500)



class Asistente_Evento(models.Model):

  id_evento = models.ForeignKey(Evento, related_name="asistentes",on_delete=models.CASCADE)
  correo = models.EmailField(max_length=100)
  nombre = models.CharField(max_length=100)
  telefono = models.CharField(max_length=20)
  metodo_pago = models.CharField(max_length=20, blank=True)
  monto_total = models.CharField(max_length=10, blank=True)
  estatus_pago = models.CharField(max_length=40, blank=True)
  fecha_agregado = models.DateTimeField(auto_now_add=True)
  fecha_actualizado = models.DateTimeField(auto_now=True)
  boletos = models.CharField(max_length=1000, blank=True)
  donacion = models.CharField(max_length=1000, blank=True)
  detalles = models.CharField(max_length=1000, blank=True)

  def __str__(self):
    return str(self.id) +""



