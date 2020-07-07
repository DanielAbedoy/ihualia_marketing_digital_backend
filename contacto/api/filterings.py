from django_filters import rest_framework as filters
import django_filters

from contacto.models import Grupo, Contacto, Grupo_Contacto, CampoExtra, CampoExtra_Grupo, Campo_Contacto


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