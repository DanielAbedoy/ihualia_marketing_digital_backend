from rest_framework import serializers

from marketing.models import Cuenta
from contacto.models import Grupo, Contacto, CampoExtra, Campo_Contacto
from marketing.api.serializers import CuentaSerializer


class ContactoSerializar(serializers.ModelSerializer):

    class Meta:
        model = Contacto
        fields = "__all__"

##Grupo
class GrupoSerializer(serializers.ModelSerializer):    

    #contactos = ContactoSerializar(required=False, many=True)

    class Meta:
        model = Grupo
        fields = "__all__"
        extra_kwargs = {'campos_extra': {'required': False}}

#Cuenta



#Campo extra
class CampoExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoExtra
        fields = '__all__'

##Campo extra contacto Valo
class Campo_ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo_Contacto
        fields = '__all__'


