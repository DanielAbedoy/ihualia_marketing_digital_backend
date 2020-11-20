from django.db import models
import json

from marketing.models import Cuenta

class Evento(models.Model):

  id_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE, related_name="evento_cuenta")
  nombre = models.CharField(max_length=200)
  tipo = models.CharField(max_length=100)
  categoria = models.CharField(max_length=70)
  sub_categoria = models.CharField(max_length=70)
  tipo_ubicacion = models.CharField(max_length=15, blank=True)
  fecha_hora_inicio = models.DateTimeField(null=True)
  fecha_hora_fin = models.DateTimeField(null=True)
  zona_horaria = models.CharField(max_length=100, blank=True)
  resumen = models.CharField(max_length=1000, blank=True)
  estatus = models.CharField(max_length=50)
  imagen = models.CharField(max_length=10, blank=True)
  url = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return str(self.id_cuenta) + " - " + self.nombre

class ImagenPrincipal(models.Model):
  evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="imegenes")
  name = models.CharField(max_length=500)



class Tags_Evento(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="etiquetas", on_delete=models.CASCADE)
  palabra = models.CharField(max_length=30)

  def __str__(self):
    return self.id_evento + " - " + self.palabra
    
class Lugar_Evento(models.Model):
  
  id_evento = models.ForeignKey(Evento, related_name="lugar",on_delete=models.CASCADE)
  direccion1 = models.CharField(max_length=200)
  direccion2 = models.CharField(max_length=200, blank=True)
  ciudad = models.CharField(max_length=60)
  estado = models.CharField(max_length=60)
  codigo_postal = models.CharField(max_length=20)
  pais = models.CharField(max_length=100)
  latitud = models.CharField(max_length=30, blank=True)
  longitud = models.CharField(max_length=30, blank=True)

  def __str__(self):
    return self.id_evento + " - " + self.codigo_postal

class Online_Evento(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="sitio",on_delete=models.CASCADE)
  link = models.CharField(max_length=200)


  def __str__(self):
    return self.id_evento + " - " + self.link

class Componente(models.Model):
  id_evento = models.ForeignKey(Evento, related_name="componentes",on_delete=models.CASCADE)
  contenido = models.CharField(max_length=4000)
  posicion = models.IntegerField()
  tipo = models.CharField(max_length=15)



class Boleto_Evento(models.Model):

  id_evento = models.ForeignKey(Evento, related_name="boletos",on_delete=models.CASCADE)
  tipo = models.CharField(max_length=50)
  nombre = models.CharField(max_length=200)
  cantida_total = models.CharField(max_length=20)
  precio = models.CharField(max_length=20)
  descripcion = models.CharField(max_length=250)
  cantidad_minima = models.CharField(max_length=20)
  cantidad_maxima = models.CharField(max_length=20)
  canal_ventas = models.CharField(max_length=50)

  def __str__(self):
    return str(self.id)+""


class Asistente_Evento(models.Model):

  id_evento = models.ForeignKey(Evento, related_name="asistentes",on_delete=models.CASCADE)
  correo = models.EmailField(max_length=100)
  nombre = models.CharField(max_length=100)
  telefono = models.CharField(max_length=20)
  metodo_pago = models.CharField(max_length=20)
  monto_total = models.CharField(max_length=10)
  estatus_pago = models.CharField(max_length=40)
  fecha_agrgado = models.DateTimeField(auto_now_add=True)
  fecha_actualizado = models.DateTimeField(auto_now=True)


  def __str__(self):
    return str(self.id) +""

class Boleto_AsistenteEvento(models.Model):

  id_asistencia = models.ForeignKey(Asistente_Evento, related_name="articulos",on_delete=models.CASCADE)
  id_boleto = models.ForeignKey(Boleto_Evento, related_name="adquiridos",on_delete=models.CASCADE)
  cantidad = models.CharField(max_length=10)

  def __str__(self):
    objeto = {"boleto":str(self.id_boleto), "asistencia":str(self.id_asistencia) ,"cantidad":self.cantidad}
    return json.dumps(objeto)

class Donacion_Asistente_Evento(models.Model):
  
  id_asistencia = models.ForeignKey(Asistente_Evento, related_name="donacion", on_delete=models.CASCADE)
  monto = models.CharField(max_length=10)

  def __str__(self):
    return str(self.id_asistencia) + " - " + self.monto


class Detalles_PagoTarjeta_Evento(models.Model):

  id_asistencia = models.ForeignKey(Asistente_Evento, related_name="detalles_card",on_delete=models.CASCADE)
  id_pago = models.CharField(max_length=60)
  id_orden = models.CharField(max_length=30)

  def __str__(self):
    return self.id_asistencia + " - " + self.id_orden


class Detalles_OxxoPay_Evento(models.Model):

  id_asistencia =models.ForeignKey(Asistente_Evento, related_name="detalles_oxxo",on_delete=models.CASCADE)
  numero_referencia = models.CharField(max_length=20)



