from django_filters import rest_framework as filters
import django_filters

from encuestas.models import Encuesta

class EncuestFiltering(filters.FilterSet):

  cuenta = filters.CharFilter(field_name="cuenta__id", lookup_expr="iexact")
  url = filters.CharFilter(field_name="url", lookup_expr="iexact")

  class Meta:
    model = Encuesta
    fields = '__all__'