from django_filters import rest_framework as filters
import django_filters

from marketing.models import Cuenta, Usuario

class UsuarioFiltering(filters.FilterSet):
    correo = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Usuario
        fields = '__all__'

class CuentaFiltering(filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='iexact')
    tipo = django_filters.CharFilter(lookup_expr='iexact')
    usuario = django_filters.CharFilter(field_name='usuario__correo',lookup_expr='iexact')

    class Meta:
        model = Cuenta
        fields = ['id','nombre','tipo','usuario']