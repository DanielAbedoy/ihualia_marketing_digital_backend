from django_filters import rest_framework as filters
import django_filters

from marketing.models import Cuenta, Usuario, Usuario_Cuenta

class UsuarioFiltering(filters.FilterSet):
    correo = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Usuario
        fields = '__all__'

class CuentaFiltering(filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='iexact')
    tipo = django_filters.CharFilter(lookup_expr='iexact')
    id_cliente = django_filters.CharFilter(lookup_expr='iexact', field_name='id_cliente__id_cliente')

    class Meta:
        model = Cuenta
        fields = '__all__'

class Usuario_Cuenta_Filtering(filters.FilterSet):

    id_usuario = django_filters.CharFilter(lookup_expr='iexact',field_name='id_usuario__correo')
    id_cuenta = django_filters.CharFilter(lookup_expr='iexact', field_name='id_cuenta__id')
    tipo = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model: Usuario_Cuenta
        fields = '__all__'