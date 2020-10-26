from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import pagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
import sys

from eventos.api.serializers import EventoSerializer, TagsEventoSerializer, LugarEventoSerializer, OnlineEventoSerializer, ParrafoEventoSerializer, VideoEventoSerializer, ImagenEventoSerializer, BoletoEventoSerializer, Asistente_EventoSerializer, Boleto_AsistenteEventoSerializer, Detalles_OxxoPay_EventoSerializer, Detalles_PagoTarjeta_EventoSerializer, Donacion_Asistente_EventoSerializer, ImagenPrincipalSerializer

from eventos.models import Evento, Tags_Evento, Lugar_Evento, Online_Evento, Parrafo_Evento, Imagen_Evento, Video_Evento, Boleto_Evento, Asistente_Evento, Boleto_AsistenteEvento, Detalles_PagoTarjeta_Evento, Detalles_OxxoPay_Evento, Donacion_Asistente_Evento, ImagenPrincipal

from eventos.api.filterings import TagsEventoFiltering, LugarEventoFiltering, OnlineEventoFiltering, ParrafoEventoFiltering, ImagenEventoFiltering, VideEventoFiltering, BoletoEventoFiltering, Boleto_Asistente_EventoFiltering, EventoFiltering, AsistenteEventoFiltering, DonacionEventoFiltering

class EventoViewSet(ModelViewSet):
  serializer_class = EventoSerializer
  queryset = Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = EventoFiltering

  
class TagsEventoViewSet(ModelViewSet):
  serializer_class = TagsEventoSerializer
  queryset = Tags_Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = TagsEventoFiltering



class LugarEventoViewSet(ModelViewSet):
  serializer_class = LugarEventoSerializer
  queryset = Lugar_Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = LugarEventoFiltering


class OnlineEventoViewSet(ModelViewSet):
  serializer_class = OnlineEventoSerializer
  queryset = Online_Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = OnlineEventoFiltering

class ParrafoEventoViewSet(ModelViewSet):
  serializer_class = ParrafoEventoSerializer
  queryset = Parrafo_Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = ParrafoEventoFiltering

class ImagenEventoViewSet(ModelViewSet):
  serializer_class = ImagenEventoSerializer
  queryset = Imagen_Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = ImagenEventoFiltering


class VideoEventoViewSet(ModelViewSet):
  serializer_class = VideoEventoSerializer
  queryset = Video_Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = VideEventoFiltering

class BoletoEventoViewSet(ModelViewSet):
  serializer_class = BoletoEventoSerializer
  queryset = Boleto_Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = BoletoEventoFiltering

class Asistente_EventoViewSet(ModelViewSet):
  serializer_class = Asistente_EventoSerializer
  queryset = Asistente_Evento.objects.all()
  filter_backend = [filters.DjangoFilterBackend]
  filterset_class = AsistenteEventoFiltering


class Boleto_AsistenteEventoViewSet(ModelViewSet):
  serializer_class = Boleto_AsistenteEventoSerializer
  queryset = Boleto_AsistenteEvento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = Boleto_Asistente_EventoFiltering

class Detalles_OxxoPay_EventoViewSet(ModelViewSet):
  serializer_class = Detalles_OxxoPay_EventoSerializer
  queryset = Detalles_OxxoPay_Evento.objects.all()

class Detalles_PagoTarjeta_EventoViewSet(ModelViewSet):
  serializer_class = Detalles_PagoTarjeta_EventoSerializer
  queryset = Detalles_PagoTarjeta_Evento.objects.all()


class Donacion_Asistente_EventoViewSet(ModelViewSet):
  serializer_class = Donacion_Asistente_EventoSerializer
  queryset = Donacion_Asistente_Evento.objects.all()
  filter_backend = [filters.DjangoFilterBackend]
  filterset_class = DonacionEventoFiltering


class ImagenPrincipalViewSet(ModelViewSet):
  serializer_class = ImagenPrincipalSerializer
  queryset = ImagenPrincipal.objects.all()