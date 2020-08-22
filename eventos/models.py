from django.db import models

from marketing.models import Cuenta

class Evento(models.Model):

  id_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE, related_name="evento_cuenta")
  nombre = models.CharField(max_length=200)
  tipo = models.CharField(max_length=100)
  categoria = models.CharField(max_length=70)
  sub_categoria = models.CharField(max_length=70)
  tipo_ubicacion = models.CharField(max_length=15)
  fecha_hora_inicio = models.DateTimeField()
  fecha_hora_fin = models.DateTimeField()
  zona_horaria = models.CharField(max_length=100)
  directorio_imagen = models.CharField(max_length=2000)
  nombre_imagen = models.CharField(max_length=500)
  resumen = models.CharField(max_length=1000)

  def __str__(self):
    return str(self.id_cuenta) + " - " + self.nombre


class Tags_Evento(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="tags_evento",on_delete=models.CASCADE)
  palabra = models.CharField(max_length=30)

  def __str__(self):
    return self.id_evento + " - " + self.plabra
    
class Lugar_Evento(models.Model):
  
  id_evento = models.ForeignKey(Evento, related_name="lugar_evento",on_delete=models.CASCADE)
  direccion1 = models.CharField(max_length=200)
  direccion2 = models.CharField(max_length=200, null=True)
  ciudad = models.CharField(max_length=60)
  estado = models.CharField(max_length=60)
  codigo_postal = models.CharField(max_length=20)
  pais = models.CharField(max_length=100)
  latitud = models.CharField(max_length=30, null=True)
  longitud = models.CharField(max_length=30, null=True)

  def __str__(self):
    return self.id_evento + " - " + self.codigo_postal

class Online_Evento(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="online_evento",on_delete=models.CASCADE)
  link = models.CharField(max_length=200)


  def __str__(self):
    return self.id_evento + " - " + self.link

class Parrafo_Evento(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="parrafo_evento",on_delete=models.CASCADE)
  parrafo = models.CharField(max_length=560)
  posicion = models.IntegerField()

  def __str__(self):
    return self.id_evento + " - " + self.parrafo

class Imagen_Evento(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="imagen_evento",on_delete=models.CASCADE)
  directorio_imagen = models.CharField(max_length=1000)
  nombre_imagen = models.CharField(max_length=500)
  posicion = models.IntegerField()

  def __str__(self):
    return self.id_evento + " - " + self.directorio_imagen

class Video_Evento(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="video_evento",on_delete=models.CASCADE)
  link = models.CharField(max_length=260)
  posicion = models.IntegerField()

  def __str__(self):
    return self.id_evento + " - " + self.link

class Boleto_Evento(models.Model):

  id_evento = models.ForeignKey(Evento, related_name="boleto_evento",on_delete=models.CASCADE)
  tipo = models.CharField(max_length=50)
  nombre = models.CharField(max_length=200)
  cantida_total = models.CharField(max_length=20)
  precio = models.CharField(max_length=20)
  descripcion = models.CharField(max_length=250)
  cantidad_minima = models.CharField(max_length=20)
  cantidad_maxima = models.CharField(max_length=20)
  canal_ventas = models.CharField(max_length=50)

  def __str__(self):
    return str(self.id)+" - " + self.nombre + " - " + self.descripcion


class Asistente_Evento(models.Model):

  id_evento = models.ForeignKey(Evento, related_name="asistente_evento",on_delete=models.CASCADE)
  correo = models.EmailField(max_length=100)
  nombre = models.CharField(max_length=100)
  telefono = models.CharField(max_length=20)
  metodo_pago = models.CharField(max_length=20)
  monto_total = models.CharField(max_length=10)
  estatus_pago = models.CharField(max_length=40)
  fecha_agrgado = models.DateTimeField(auto_now_add=True)
  fecha_actualizado = models.DateTimeField(auto_now=True)


  def __str__(self):
    return str(self.id_evento) + " - " + self.correo

class Boleto_AsistenteEvento(models.Model):

  id_asistencia = models.ForeignKey(Asistente_Evento, related_name="boleto_asistente",on_delete=models.CASCADE)
  id_boleto = models.ForeignKey(Boleto_Evento, related_name="boleto_item",on_delete=models.CASCADE)
  cantidad = models.CharField(max_length=10)

  def __str__(self):
    return str(self.id_asistencia) + " - " + str(self.id_boleto) + " - " + self.cantidad

class Donacion_Asistente_Evento(models.Model):
  
  id_asistencia = models.ForeignKey(Asistente_Evento, related_name="donacion_asistente", on_delete=models.CASCADE)
  monto = models.CharField(max_length=10)

  def __str__(self):
    return str(self.id_asistencia) + " - " + self.monto


class Detalles_PagoTarjeta_Evento(models.Model):

  id_asistencia = models.ForeignKey(Asistente_Evento, related_name="cardDetailspay_asistente",on_delete=models.CASCADE)
  id_pago = models.CharField(max_length=60)
  id_orden = models.CharField(max_length=30)

  def __str__(self):
    return self.id_asistencia + " - " + self.id_orden


class Detalles_OxxoPay_Evento(models.Model):

  id_asistencia =models.ForeignKey(Asistente_Evento, related_name="oxxoDetails_asistente",on_delete=models.CASCADE)
  numero_referencia = models.CharField(max_length=20)



