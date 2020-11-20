from django_filters import rest_framework as filters
import django_filters


from  eventos.models import Evento, Tags_Evento, Boleto_Evento, Lugar_Evento, Online_Evento, Boleto_AsistenteEvento, Asistente_Evento, Donacion_Asistente_Evento

class TagsEventoFiltering(filters.FilterSet):
  
  id_evento = filters.CharFilter(field_name="id_evento__id",lookup_expr="iexact")
  class Meta:
    model = Tags_Evento
    fields = '__all__'
    
class LugarEventoFiltering(filters.FilterSet):
  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Lugar_Evento
    fields = '__all__'


class OnlineEventoFiltering(filters.FilterSet):
  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Online_Evento
    fields = '__all__'

class BoletoEventoFiltering(filters.FilterSet):
  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Boleto_Evento
    fields = '__all__'

class Boleto_Asistente_EventoFiltering(filters.FilterSet):
  id_boleto = filters.CharFilter(field_name="id_boleto__id", lookup_expr='iexact')
  id_asistencia = filters.CharFilter(field_name="id_asistencia__id",lookup_expr="iexact")
  class Meta:
    model = Boleto_AsistenteEvento
    fields = '__all__'


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

class DonacionEventoFiltering(filters.FilterSet):
  id_asistencia = filters.CharFilter(field_name="id_asistencia__id", lookup_expr="iexact")

  class Meta:
    model = Donacion_Asistente_Evento
    fields = '__all__'

