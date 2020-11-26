from django_filters import rest_framework as filters
import django_filters

from emailmarketing.models import  Boletin

class BoletinFiltering(filters.FilterSet):

  id_cuenta = filters.CharFilter(field_name="id_cuenta__id", lookup_expr="iexact")
  fecha_start = django_filters.DateFilter(field_name="fecha_creado", lookup_expr="gte")
  fecha_end = django_filters.DateFilter(field_name="fecha_creado", lookup_expr="lte")

  class Meta:
    model = Boletin
    fields = '__all__'

