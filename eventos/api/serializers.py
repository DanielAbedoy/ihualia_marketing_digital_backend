from rest_framework import serializers

from eventos.models import Evento, Tags_Evento, Lugar_Evento, Online_Evento, Parrafo_Evento, Imagen_Evento, Video_Evento, Boleto_Evento, Asistente_Evento,Boleto_AsistenteEvento, Detalles_OxxoPay_Evento, Detalles_PagoTarjeta_Evento, Donacion_Asistente_Evento

class EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Evento
    fields = '__all__'

class TagsEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tags_Evento
    fields = '__all__'

class LugarEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lugar_Evento
    fields = '__all__'

class OnlineEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Online_Evento
    fields = '__all__'

class ParrafoEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Parrafo_Evento
    fields = '__all__'

class ImagenEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Imagen_Evento
    fields = '__all__'

class VideoEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video_Evento
    fields = '__all__'

class BoletoEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Boleto_Evento
    fields = '__all__'

class Asistente_EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Asistente_Evento
    fields= '__all__'

class Boleto_AsistenteEventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Boleto_AsistenteEvento
    fields = '__all__'

class Detalles_OxxoPay_EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Detalles_OxxoPay_Evento
    fields = '__all__'

class Detalles_PagoTarjeta_EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Detalles_PagoTarjeta_Evento
    fields = '__all__'


class Donacion_Asistente_EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Donacion_Asistente_Evento
    fields = '__all__'