from rest_framework import serializers

from eventos.models import Evento, Asistente_Evento, ImagenPrincipal


class ImagenPrincipalSerializer(serializers.ModelSerializer):

  class Meta:
    model = ImagenPrincipal
    fields = '__all__'



class Asistente_EventoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Asistente_Evento
    fields= '__all__'


class EventoSerializer(serializers.ModelSerializer):

  asistentes = Asistente_EventoSerializer(required=False, many=True)

  class Meta:
    model = Evento
    fields = '__all__'