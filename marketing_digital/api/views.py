from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import pagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
import sys

from marketing_digital.models import (
  Usuario, Cuenta, Cliente, Usuario_Cuenta,
  Grupo, Contacto, Grupo_Contacto, CampoExtra, CampoExtra_Grupo, Campo_Contacto,
)

from marketing_digital.api.serializers import (
  UsuarioSerializar, CuentaSerializer, ClienteSerializer, Usuario_Cuenta_Serializer,
  GrupoSerializer, GrupoPostSerializer, ContactoSerializar, Grupo_ContactoSerializer, GrupoContacto_PostSerializer, CampoExtraSerializer, CampoExtra_GrupoSerializer, CampoExtra_Grupo_PostSerializer, Campo_ContactoSerializer, Campo_Contacto_PostSerializer,
)

from marketing_digital.api.filterings import (
  CuentaFiltering, UsuarioFiltering, Usuario_Cuenta_Filtering,
  GrupoFiltering,ContactoFiltering,Grupo_ContactoFiltering,CampoExtra_GrupoFiltering,Campo_ContactoFilterin
)

##Pagination
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 2500

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

#Vistas para el modelo __Usuario__
class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializar
    queryset = Usuario.objects.all()
    lookup_field = 'correo'
    lookup_url_kwarg = 'correo'
    lookup_value_regex = '[\w@.]+' # here is the new attribute
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UsuarioFiltering

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    queryset = Cuenta.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CuentaFiltering

class Usuario_Cuenta_ViewSet(viewsets.ModelViewSet):
    serializer_class = Usuario_Cuenta_Serializer
    queryset = Usuario_Cuenta.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = Usuario_Cuenta_Filtering

class GrupoViewSet(viewsets.ModelViewSet):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = GrupoFiltering
class GrupoPostView(CreateAPIView):
    serializer_class = GrupoPostSerializer
    queryset = Grupo.objects.all()

    
#Contacto
class ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactoSerializar
    queryset = Contacto.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ContactoFiltering


#Grupo contacto
class GrupoContactoViewSet(viewsets.ModelViewSet):
    serializer_class = Grupo_ContactoSerializer
    queryset = Grupo_Contacto.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = Grupo_ContactoFiltering
class GrupoContacto_PostView(APIView):
    def post(self, request, format=None):
        serializer = GrupoContacto_PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Campo Extra
class CampoExtraViewSet(viewsets.ModelViewSet):
    serializer_class = CampoExtraSerializer
    queryset = CampoExtra.objects.all()


##Campo extra grupo 
class CampoExtra_GrupoViewSet(viewsets.ModelViewSet):
    serializer_class = CampoExtra_GrupoSerializer
    queryset = CampoExtra_Grupo.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CampoExtra_GrupoFiltering

class CampoExtra_Grupo_PostView(APIView):
    def post(self, request, format=None):
        serializer = CampoExtra_Grupo_PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Campo_ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = Campo_ContactoSerializer
    queryset = Campo_Contacto.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = Campo_ContactoFilterin
class Campo_Contacto_PostView(CreateAPIView):
    serializer_class = Campo_Contacto_PostSerializer
    queryset = Campo_Contacto.objects.all()

