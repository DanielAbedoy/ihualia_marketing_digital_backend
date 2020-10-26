from rest_framework import serializers

from marketing.models import Cuenta

from contacto.models import Grupo, Contacto, Grupo_Contacto, CampoExtra, CampoExtra_Grupo, Campo_Contacto
from marketing.api.serializers import CuentaSerializer
#Contacto, GrupoContacto, CampoExtra, CampoExtra_Contacto, GrupoCampoExtra

##Grupo
class GrupoSerializer(serializers.ModelSerializer):

    cuenta = CuentaSerializer(many=False,read_only=True,required=False)
    class Meta:
        model = Grupo
        fields = ('id', 'nombre', 'cuenta')
class GrupoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ('id', 'nombre', 'cuenta')

#Cuenta
class ContactoSerializar(serializers.ModelSerializer):
    campos_extra = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Contacto
        fields = '__all__'

##Grupo Contacto
class Grupo_ContactoSerializer(serializers.ModelSerializer):
    contacto = ContactoSerializar(many=False,read_only=False)
    grupo  = GrupoSerializer(many=False,read_only=False)
    class Meta:
        model = Grupo_Contacto
        fields = ['id', 'contacto', 'grupo']
class GrupoContacto_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo_Contacto
        fields = '__all__'


#Campo extra
class CampoExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoExtra
        fields = '__all__'


#CanpoExtra Grupo
class CampoExtra_GrupoSerializer(serializers.ModelSerializer):
    grupo = GrupoSerializer(many=False)
    class Meta:
        model = CampoExtra_Grupo
        fields = '__all__'
class CampoExtra_Grupo_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoExtra_Grupo
        fields = '__all__'

##Campo extra contacto Valo
class Campo_ContactoSerializer(serializers.ModelSerializer):
    contacto = ContactoSerializar(many=False,required=False)
    class Meta:
        model = Campo_Contacto
        fields = '__all__'

class Campo_Contacto_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo_Contacto
        fields = '__all__'

