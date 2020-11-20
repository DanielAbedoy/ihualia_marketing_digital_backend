from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import pagination
from django_filters import rest_framework as filters

from marketing.models import Usuario, Cuenta, Cliente,CuentaUsuario
from .serializers import UsuarioSerializar, CuentaSerializer, ClienteSerializer, CuentaUsuarioSerializer
from .filterings import CuentaFiltering, UsuarioFiltering

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
    #lookup_field = 'correo'
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

class CuentaUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaUsuarioSerializer
    queryset = CuentaUsuario.objects.all()

    @action(detail=False, methods=["post"])
    def addcuentas(self, request):
        
        user = request.data["usuario"]
        cuentas = request.data["cuentas"]

        responses = []
        for cuenta in cuentas:
            serializer = CuentaUsuarioSerializer(data={"cuenta": cuenta["id"], "usuario":user, "tipo":cuenta["tipo"]})
            
            if serializer.is_valid():
                serializer.save()
                responses.append({"cuenta": cuenta["id"], "status": "Created"})
            else:
                responses.append({"cuenta": cuenta["id"], "status": "error", "error": serializer.errors})

        return Response(responses,status=status.HTTP_201_CREATED)    



    @action(detail=False, methods=["post"])
    def addusers(self, request):
        cuenta = request.data["cuenta"]
        nuevos = request.data["allnew"]
        responses = []
        for nuevo in nuevos:
            serializer = CuentaUsuarioSerializer(data={"cuenta": cuenta, "usuario": nuevo["user"], "tipo": nuevo["tipo"]})
            if serializer.is_valid():
                serializer.save()
                responses.append({"user": nuevo["user"], "status": "Created"})
            else:
                responses.append({"user": nuevo["user"], "status": "Error", "error": serializer.errors})

        return Response(responses,status=status.HTTP_201_CREATED)    

    
    @action(detail=False, methods=['get'])
    def usuarios(self, request, format=None):
        
        cuenta = request.query_params.get('cuenta')
        queryset = CuentaUsuario.objects.filter(cuenta=cuenta)
        serializer = CuentaUsuarioSerializer(queryset, many=True)

        response =[]
        for registro in serializer.data:
            user = registro["usuario"]
            querysetUser = Usuario.objects.get(correo=user)
            serializerUser = UsuarioSerializar(querysetUser, many=False)
            data = serializerUser.data
            response.append({"correo":data["correo"],"nombre":data["nombre"],"estatus":data["estatus"], "tipo":registro["tipo"]})

        return Response(response,status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def cuentas(self, request):

        usuario = request.query_params.get('usuario')
        queryset = CuentaUsuario.objects.filter(usuario=usuario)
        serializer = CuentaUsuarioSerializer(queryset, many=True)
        
        response = []
        for registro in serializer.data:
            cuenta = registro["cuenta"]
            querysetCuenta = Cuenta.objects.get(id=cuenta)
            serializerCuenta = CuentaSerializer(querysetCuenta, many=False)
            data = serializerCuenta.data
            response.append({"id": data["id"], "nombre": data["nombre"], "estatus": data["estatus"], "tipo":registro["tipo"]})
        
        return Response(response, status=status.HTTP_200_OK)