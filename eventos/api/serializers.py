from rest_framework import serializers

from eventos.models import Evento, Tags_Evento, Lugar_Evento, Online_Evento, Componente, Boleto_Evento, Asistente_Evento,Boleto_AsistenteEvento, Detalles_OxxoPay_Evento, Detalles_PagoTarjeta_Evento, Donacion_Asistente_Evento, ImagenPrincipal


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

class ComponenteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Componente
    fields = '__all__'

class BoletoEventoSerializer(serializers.ModelSerializer):

  adquiridos = serializers.StringRelatedField(many=True, required=False)

  class Meta:
    model = Boleto_Evento
    fields = '__all__'

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


class ImagenPrincipalSerializer(serializers.ModelSerializer):

  class Meta:
    model = ImagenPrincipal
    fields = '__all__'



class Asistente_EventoSerializer(serializers.ModelSerializer):

  donacion = Donacion_Asistente_EventoSerializer(required=False, many=True)
  articulos = serializers.StringRelatedField(many=True, required=False)


  class Meta:
    model = Asistente_Evento
    fields= '__all__'




class EventoSerializer(serializers.ModelSerializer):

  etiquetas = TagsEventoSerializer(required=False, many=True)
  lugar = LugarEventoSerializer(required=False, many=True)
  sitio = OnlineEventoSerializer(required=False, many=True)
  componentes = ComponenteSerializer(required=False, many=True)
  boletos = BoletoEventoSerializer(required=False, many=True)
  asistentes = Asistente_EventoSerializer(required=False, many=True)

  class Meta:
    model = Evento
    fields = '__all__'