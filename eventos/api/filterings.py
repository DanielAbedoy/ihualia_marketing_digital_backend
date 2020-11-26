from django_filters import rest_framework as filters
import django_filters


from  eventos.models import Evento, Asistente_Evento


##Nuevos cambios

class EventoFiltering(filters.FilterSet):

  id_cuenta = filters.CharFilter(field_name="id_cuenta__id", lookup_expr="iexact")
  url = filters.CharFilter(field_name="url", lookup_expr="iexact")
  class Meta:
    model= Evento
    fields="__all__"


class AsistenteEventoFiltering(filters.FilterSet):

  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Asistente_Evento
    fields = '__all__'
