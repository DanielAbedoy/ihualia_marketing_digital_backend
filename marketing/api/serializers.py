from rest_framework import serializers

from marketing.models import Usuario, Cuenta

class UsuarioSerializar(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'
