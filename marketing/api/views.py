from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework import pagination
from django_filters import rest_framework as filters

from marketing.models import Usuario, Cuenta, Cliente, Usuario_Cuenta
from .serializers import UsuarioSerializar, CuentaSerializer, ClienteSerializer, Usuario_Cuenta_Serializer
from .filterings import CuentaFiltering, UsuarioFiltering, Usuario_Cuenta_Filtering

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