from django_filters import rest_framework as filters
import django_filters

from contacto.models import Grupo, Contacto, CampoExtra, Campo_Contacto


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


class Campo_ContactoFilterin(filters.FilterSet):

    contacto = django_filters.CharFilter(lookup_expr='iexact', field_name='contacto__id')
    campo = django_filters.CharFilter(lookup_expr='iexact', field_name='campo__nombre')
    class Meta:
        model = Campo_Contacto
        fields = ['contacto','campo']