from django_filters import rest_framework as filters
import django_filters

from emailmarketing.models import FechaHoraPublicacionBoletin,  Boletin, EnvioBoletin, SeenContactoBoletin, LinkBoletin, SeenLinkBoletin

class BoletinFiltering(filters.FilterSet):

  id_cuenta = filters.CharFilter(field_name="id_cuenta__id", lookup_expr="iexact")
  fecha_start = django_filters.DateFilter(field_name="fecha_creado", lookup_expr="gte")
  fecha_end = django_filters.DateFilter(field_name="fecha_creado", lookup_expr="lte")

  class Meta:
    model = Boletin
    fields = '__all__'


class FechaHoraPublicacionBoletinFiltering(filters.FilterSet):

  fecha = django_filters.DateFilter(field_name="fecha", lookup_expr="iexact")
  hora = filters.CharFilter(field_name="hora",lookup_expr="iexact")

  class Meta:
    model = FechaHoraPublicacionBoletin
    fields = '__all__'

class EnvioBoletinFilterin(filters.FilterSet):
  id_boletin = filters.CharFilter(field_name="id_boletin__id", lookup_expr="iexact")
  
  class Meta:
    model = EnvioBoletin
    fields = '__all__'

class SeenContactoBoletinFiltering(filters.FilterSet):

  id_boletin = filters.CharFilter(field_name="id_boletin__id", lookup_expr="iexact")
  class Meta:
    model = SeenContactoBoletin
    fields = '__all__'

class LinkBoletinFiltering(filters.FilterSet):
  id_boletin = filters.CharFilter(field_name="id_boletin__id", lookup_expr="iexact")
  class Meta:
    model = LinkBoletin
    fields = '__all__'

class SeenLinkBoletinFiltering(filters.FilterSet):
  id_link = filters.CharFilter(field_name="id_link__id", lookup_expr="iexact")
  class Meta:
    model = SeenLinkBoletin
    fields = '__all__'