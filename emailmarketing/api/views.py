from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import pagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
import sys

from emailmarketing.api.serializers import (
  BoletinSerializer, ImagenBoletinSerializer,
  SeenContactoBoletinSerializer, SeenLinkBoletinSerializer
)

from emailmarketing.models import (
  Boletin,
  ImagenBoletin, SeenContactoBoletin, SeenLinkBoletin
)

from emailmarketing.api.filterings import (
   BoletinFiltering, 
)

class BoletinViewSet(ModelViewSet):
  
    serializer_class = BoletinSerializer
    queryset = Boletin.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BoletinFiltering


class ImagenBoletinViewSet(ModelViewSet):
  serializer_class = ImagenBoletinSerializer
  queryset = ImagenBoletin.objects.all()



class SeenContactoBoletinViewSet(ModelViewSet):
  serializer_class = SeenContactoBoletinSerializer
  queryset = SeenContactoBoletin.objects.all()


class SeenLinkBoletinViewSet(ModelViewSet):
  serializer_class = SeenLinkBoletinSerializer
  queryset =SeenLinkBoletin .objects.all()
  



