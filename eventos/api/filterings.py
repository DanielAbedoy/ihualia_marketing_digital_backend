from django_filters import rest_framework as filters
import django_filters


from  eventos.models import Evento, Tags_Evento, Imagen_Evento, Video_Evento, Parrafo_Evento, Boleto_Evento, Lugar_Evento, Online_Evento, Boleto_AsistenteEvento

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

class ParrafoEventoFiltering(filters.FilterSet):
  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Parrafo_Evento
    fields = '__all__'

class ImagenEventoFiltering(filters.FilterSet):
  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Imagen_Evento
    fields = '__all__'

class VideEventoFiltering(filters.FilterSet):
  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Video_Evento
    fields = '__all__'

class BoletoEventoFiltering(filters.FilterSet):
  id_evento = filters.CharFilter(field_name="id_evento__id", lookup_expr="iexact")
  class Meta:
    model = Boleto_Evento
    fields = '__all__'

class Boleto_Asistente_EventoFiltering(filters.FilterSet):
  id_boleto = filters.CharFilter(field_name="id_boleto__id", lookup_expr='iexact')
  class Meta:
    model = Boleto_AsistenteEvento
    fields = '__all__'
