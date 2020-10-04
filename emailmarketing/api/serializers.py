from rest_framework import serializers

from emailmarketing.models import (
  Boletin, FechaHoraPublicacionBoletin, GrupoEnvioBoletin,
  ImagenBoletin, LinkBoletin, PlantillaBoletin, SeenContactoBoletin,
   SeenLinkBoletin, EnvioBoletin
)

from contacto.api.serializers import ContactoSerializar

class BoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = Boletin
    fields = '__all__'

class EnvioBoletinSerializer(serializers.ModelSerializer):
  class Meta:
    model = EnvioBoletin
    fields = '__all__'



class FechaHoraPublicacionBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = FechaHoraPublicacionBoletin
    fields = '__all__'

class GrupoEnvioBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = GrupoEnvioBoletin
    fields = '__all__'

class PlantillaBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = PlantillaBoletin
    fields = '__all__'

class ImagenBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = ImagenBoletin
    fields = '__all__'

class LinkBoletinSerializer(serializers.ModelSerializer):

  class Meta:
    model = LinkBoletin
    fields = '__all__'


class SeenContactoBoletinPostSerializer(serializers.ModelSerializer):

  class Meta:
    model = SeenContactoBoletin
    fields = '__all__'

class SeenLinkBoletinPostSerializer(serializers.ModelSerializer):

  class Meta:
    model = SeenLinkBoletin
    fields = '__all__'


class SeenContactoBoletinSerializer(serializers.ModelSerializer):

  id_contacto = ContactoSerializar(many=False, read_only=False)
  id_boletin = BoletinSerializer(many=False,read_only=False)

  class Meta:
    model = SeenContactoBoletin
    fields = '__all__'

class SeenLinkBoletinSerializer(serializers.ModelSerializer):

  id_link = LinkBoletinSerializer(many=False, read_only=False)
  id_contacto = ContactoSerializar(many=False, read_only=False)

  class Meta:
    model = SeenLinkBoletin
    fields = '__all__'


