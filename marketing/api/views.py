from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework import pagination
from django_filters import rest_framework as filters

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.hashers import make_password, check_password

from marketing.models import Usuario, Cuenta, Cliente,CuentaUsuario
from .serializers import UsuarioSerializar, CuentaSerializer, ClienteSerializer, CuentaUsuarioSerializer
from .filterings import CuentaFiltering, UsuarioFiltering

##Pagination
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 2500


@api_view(["POST"])
@permission_classes([AllowAny])
def createFirst(request):
    d = request.data
    r = {}
    statusR = ''

    serializer = ClienteSerializer(data={"nombre": d["nombre"], "razon_social": d["razon_social"], "direccion": d["direccion"], "telefono": d["telefono"], "dominio": d["dominio"], "giro": d["giro"]})
    
    if serializer.is_valid():
        serializer.save()
        serializerUser = UsuarioSerializar(data={"nombre": d["nombre"], "correo": d["correo"], "usuario": d["usuario"], "tipo": d["tipo"], "estatus": d["estatus"], "imagen": d["imagen"], "password": make_password(d["password"]),"id_cliente": serializer.data["id_cliente"]})
        if serializerUser.is_valid():
            serializerUser.save()
            r["status"] = "OK"
            statusR = status.HTTP_201_CREATED
        else:
            r["error"] = serializerUser.errors
            statusR = status.HTTP_400_BAD_REQUEST
    else:
        r["error"] = serializer.errors
        statusR = status.HTTP_400_BAD_REQUEST

    return Response(r, status=statusR)
    

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

    @action(detail=True, methods=["get"])
    def info(relf, request, pk=None):
        c = Cliente.objects.get(id_cliente=pk)
        return Response({"id":c.id_cliente,"razon_social": c.razon_social,"direccion": c.direccion,"telefono": c.telefono,"dominio": c.dominio,"giro": c.giro})


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializar
    queryset = Usuario.objects.all()
    #lookup_field = 'correo'
    #lookup_url_kwarg = 'correo'
    #lookup_value_regex = '[\w@.]+' # here is the new attribute
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UsuarioFiltering

    @action(detail=True, methods=["PATCH"])
    def actualizar(self, request, pk=None):

        queryset = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializar(queryset)
        r = {}
        
        info = request.data

        if ("password" in info):
            if (check_password(info["password"], serializer.data["password"]) == True):
                serializerToUpdate = UsuarioSerializar(instance=queryset, data={"password":make_password(info["password_new"])}, partial=True)
                if serializerToUpdate.is_valid():
                    serializerToUpdate.save()
                    r["message"] = "Actualizada correctamente"
                else:
                    r["error"] = serializer.errors    
            else:
                r["error"] = "La contraseña principal no es la correcta"
        else:
            data = {}
            for key in info:
                data[key] = info[key]

            serializerToUpdate = UsuarioSerializar(instance=queryset, data=data, partial=True)
            if serializerToUpdate.is_valid():
                serializerToUpdate.save()
                r["message"] = "Actualizado correctamente"
            else:
                r["error"] = serializerToUpdate.errors 

        return Response(r)

    @action(detail=True, methods=["get"])
    def info(self,request, pk=None):

        u = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializar(u)
        return Response({"id": u.id,"correo": u.correo,"usuario": u.usuario,"nombre": u.nombre,"tipo": u.tipo,"estatus": u.estatus,"imagen": u.imagen,"descripcion": u.descripcion, "cuentas": serializer.data["cuentas"]})

    @action(detail=False, methods=["get"])
    def bycliente(self, request):
        
        r = []
        users = Usuario.objects.filter(id_cliente=request.query_params.get("cliente"))
        for u in users:
            serilizer = UsuarioSerializar(u)
            r.append({"id": u.id,"correo": u.correo,"usuario": u.usuario,"nombre": u.nombre,"tipo": u.tipo,"estatus": u.estatus,"imagen": u.imagen,"descripcion": u.descripcion, "cuentas":serilizer.data["cuentas"]})

        return Response(r)

    @action(detail=False, methods=["post"])
    def createnew(self, request):

        d = request.data
        serializer = UsuarioSerializar(data={"correo": d["correo"], "usuario": d["usuario"], "password": make_password(d["password"]), "nombre": d["nombre"], "tipo": "colaborador", "estatus": "activo", "imagen": d["imagen"], "id_cliente": d["cliente"]})
        response = {}
        
        if serializer.is_valid():
            user = serializer.save()

            for c in d["cuentas"]:
                serializerC = CuentaUsuarioSerializer(data={"cuenta": c["cuenta"], "usuario":user.id, "tipo":c["cargo"]})
                if serializerC.is_valid():
                    serializerC.save()
            response["message"] = "Creado"
        else:
            response["error"] = serializer.errors

        return Response(response)
        

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    queryset = Cuenta.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CuentaFiltering

    @action(detail=False, methods=["post"])
    def createnew(self, request):
        
        d = request.data
        serializer = CuentaSerializer(data={"nombre": d["nombre"], "estatus": "Activo", "id_cliente": d["cliente"]})
        response = {}

        if serializer.is_valid():
            cuenta = serializer.save()

            for u in d["usuarios"]:
                serializerC = CuentaUsuarioSerializer(data={"cuenta": cuenta.id, "usuario":u["usuario"], "tipo":u["cargo"]})
                if serializerC.is_valid():
                    serializerC.save()
            response["message"] = "Creado"
        else:
            response["error"] = serializer.errors

        return Response(response)

    @action(detail=True, methods=["get"])
    def organzador(self, request, pk=None):
        c = Cuenta.objects.get(id=pk)
        return Response({"nombre": c.nombre})
    

class CuentaUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaUsuarioSerializer
    queryset = CuentaUsuario.objects.all()

    @action(detail=False, methods=["post"])
    def addcuentas(self, request):
        
        user = request.data["usuario"]
        cuentas = request.data["cuentas"]
        estatus = ""
        responses = []
        for cuenta in cuentas:
            serializer = CuentaUsuarioSerializer(data={"cuenta": cuenta["cuenta"], "usuario":user, "tipo":cuenta["cargo"]})
            
            if serializer.is_valid():
                serializer.save()
                responses.append({"cuenta": cuenta["cuenta"], "status": "Created"})
                estatus = status.HTTP_201_CREATED
            else:
                responses.append({"cuenta": cuenta["cuenta"], "status": "error", "error": serializer.errors})
                estatus = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(responses,status=estatus)    



    @action(detail=False, methods=["post"])
    def addusers(self, request):
        cuenta = request.data["cuenta"]
        nuevos = request.data["usuarios"]
        responses = []
        estatus = ""
        for nuevo in nuevos:
            serializer = CuentaUsuarioSerializer(data={"cuenta": cuenta, "usuario": nuevo["usuario"], "tipo": nuevo["cargo"]})
            if serializer.is_valid():
                serializer.save()                
                responses.append({"user": nuevo["usuario"], "status": "Created"})
                estatus = status.HTTP_201_CREATED
            else:
                responses.append({"user": nuevo["usuario"], "status": "Error", "error": serializer.errors})
                estatus = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(responses,status=estatus)    

    
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

    @action(detail=False, methods=["post"])
    def desvincular(self, request):
        d = request.data
        print(d)
        query = CuentaUsuario.objects.get(cuenta=d["cuenta"], usuario=d["usuario"])
        query.delete()
        return Response(status.HTTP_204_NO_CONTENT)

