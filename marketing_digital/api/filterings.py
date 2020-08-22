from django_filters import rest_framework as filters
import django_filters

from marketing_digital.models import (
  Cuenta, Usuario, Usuario_Cuenta,
  Grupo, Contacto, Grupo_Contacto, CampoExtra, CampoExtra_Grupo, Campo_Contacto
)


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

##Filtros del Grupo
class GrupoFiltering(filters.FilterSet):

    nombre = django_filters.CharFilter(lookup_expr='iexact')
    cuenta = django_filters.CharFilter(field_name='cuenta__id', lookup_expr='iexact')

    class Meta:
        model = Grupo
        fields = ['nombre', 'cuenta']
        
class ContactoFiltering(filters.FilterSet):

    nombre = django_filters.CharFilter(lookup_expr='iexact')
    correo = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Contacto
        fields = ['nombre','correo']

class Grupo_ContactoFiltering(filters.FilterSet):

    contacto = django_filters.CharFilter(lookup_expr='iexact', field_name='contacto__correo')
    grupo = django_filters.CharFilter(lookup_expr='iexact', field_name='grupo__id')

    class Meta:
        model = Grupo_Contacto
        fields = ['contacto', 'grupo']

class CampoExtra_GrupoFiltering(filters.FilterSet):
    campo_extra = django_filters.CharFilter(lookup_expr='iexact', field_name='campo_extra__nombre')
    grupo = django_filters.CharFilter(lookup_expr='iexact', field_name='grupo__id')
    
    class Meta:
        model = CampoExtra_Grupo
        fields = ['campo_extra', 'grupo']

class Campo_ContactoFilterin(filters.FilterSet):

    contacto = django_filters.CharFilter(lookup_expr='iexact', field_name='contacto__id')
    campo = django_filters.CharFilter(lookup_expr='iexact', field_name='campo__nombre')
    class Meta:
        model = Campo_Contacto
        fields = ['contacto','campo']