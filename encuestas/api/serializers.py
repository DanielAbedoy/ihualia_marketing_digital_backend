from rest_framework import serializers

from encuestas.models import Imagen, Encuesta, Encuestado


class ImagenSerializer(serializers.ModelSerializer):

  class Meta:
    model = Imagen
    fields = '__all__'
    

class EncuestadoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Encuestado
    fields='__all__'

class EncuestaSerializer(serializers.ModelSerializer):

  encuestados = EncuestadoSerializer(many=True, required=False)

  class Meta:
    model = Encuesta
    fields = '__all__'
