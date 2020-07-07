from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework import pagination
from django_filters import rest_framework as filters

from marketing.models import Usuario, Cuenta
from .serializers import UsuarioSerializar, CuentaSerializer
from .filterings import CuentaFiltering, UsuarioFiltering

##Pagination
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 2500



#Vistas para el modelo __Usuario__
class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializar
    queryset = Usuario.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UsuarioFiltering

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    queryset = Cuenta.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CuentaFiltering
