from rest_framework import serializers

from emailmarketing.models import (
  Boletin,
  ImagenBoletin, SeenContactoBoletin,
   SeenLinkBoletin
)

from contacto.api.serializers import ContactoSerializar


class ImagenBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = ImagenBoletin
    fields = '__all__'


class SeenContactoBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = SeenContactoBoletin
    fields = '__all__'

class SeenLinkBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = SeenLinkBoletin
    fields = '__all__'


class BoletinSerializer(serializers.ModelSerializer):

  links_vistos = SeenLinkBoletinSerializer(many=True, read_only=True)
  contactos_vistos = SeenContactoBoletinSerializer(many=True, read_only=True)

  class Meta:
    model = Boletin
    fields = '__all__'

