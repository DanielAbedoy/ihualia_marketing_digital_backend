from rest_framework import serializers

from marketing.models import Usuario, Cuenta, Cliente, CuentaUsuario


class UsuarioSerializar(serializers.ModelSerializer):

    cuentas = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Usuario
        fields = '__all__'


class CuentaSerializer(serializers.ModelSerializer):
    
    usuarios = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Cuenta
        fields = '__all__'
        

class ClienteSerializer(serializers.ModelSerializer):

    usuarios = UsuarioSerializar(many=True, required=False)
    cuentas = CuentaSerializer(many=True, required=False)
    class Meta:
        model = Cliente
        fields = '__all__'

class CuentaUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = CuentaUsuario
        fields = ("usuario","cuenta","tipo")