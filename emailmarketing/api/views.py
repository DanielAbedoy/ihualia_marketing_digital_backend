from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import pagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
import sys

from emailmarketing.api.serializers import (
  BoletinSerializer, FechaHoraPublicacionBoletinSerializer, GrupoEnvioBoletinSerializer,
  PlantillaBoletinSerializer, ImagenBoletinSerializer, LinkBoletinSerializer, SeenContactoBoletinPostSerializer,
  SeenContactoBoletinSerializer, SeenLinkBoletinPostSerializer, SeenLinkBoletinSerializer, EnvioBoletinSerializer

)

from emailmarketing.models import (
  Boletin, FechaHoraPublicacionBoletin, GrupoEnvioBoletin,
  ImagenBoletin, LinkBoletin, PlantillaBoletin, SeenContactoBoletin,
   SeenLinkBoletin, EnvioBoletin
)

from emailmarketing.api.filterings import (
  FechaHoraPublicacionBoletinFiltering, BoletinFiltering, EnvioBoletinFilterin,
  SeenContactoBoletinFiltering, LinkBoletinFiltering, SeenLinkBoletinFiltering
)

class BoletinViewSet(ModelViewSet):
  
    serializer_class = BoletinSerializer
    queryset = Boletin.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BoletinFiltering

class EnvioBoletinViewSet(ModelViewSet):

  serializer_class = EnvioBoletinSerializer
  queryset = EnvioBoletin.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = EnvioBoletinFilterin

class GrupoEnvioBoletinViewSet(ModelViewSet):
  serializer_class = GrupoEnvioBoletinSerializer
  queryset = GrupoEnvioBoletin.objects.all()

class FechaHoraPublicacionBoletinViewSet(ModelViewSet):
  serializer_class = FechaHoraPublicacionBoletinSerializer
  queryset = FechaHoraPublicacionBoletin.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = FechaHoraPublicacionBoletinFiltering



class PlantillaBoletinViewSet(ModelViewSet):
  serializer_class = PlantillaBoletinSerializer
  queryset = PlantillaBoletin.objects.all()

class ImagenBoletinViewSet(ModelViewSet):
  serializer_class = ImagenBoletinSerializer
  queryset = ImagenBoletin.objects.all()

class LinkBoletinViewSet(ModelViewSet):
  serializer_class = LinkBoletinSerializer
  queryset = LinkBoletin.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class= LinkBoletinFiltering



class SeenContactoBoletinViewSet(ModelViewSet):
  serializer_class = SeenContactoBoletinSerializer
  queryset = SeenContactoBoletin.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = SeenContactoBoletinFiltering


class SeenContactoBoletinPostView(CreateAPIView):
  serializer_class = SeenContactoBoletinPostSerializer
  queryset = SeenContactoBoletin.objects.all()
  


class SeenLinkBoletinViewSet(ModelViewSet):
  serializer_class = SeenLinkBoletinSerializer
  queryset = SeenLinkBoletin.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = SeenLinkBoletinFiltering


class SeenLinkBoletinPostView(CreateAPIView):
  serializer_class = SeenLinkBoletinPostSerializer
  queryset = SeenLinkBoletin.objects.all()


