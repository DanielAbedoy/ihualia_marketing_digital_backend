from rest_framework import serializers

from marketing.models import Usuario, Cuenta, Usuario_Cuenta, Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class UsuarioSerializar(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class Usuario_Cuenta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Cuenta
        fields = '__all__'