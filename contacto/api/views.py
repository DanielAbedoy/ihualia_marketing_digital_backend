from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import pagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
import sys
from django.core.exceptions import ObjectDoesNotExist

#Modelos
from marketing.models import Cuenta
from contacto.models import (
    Grupo,
    Contacto,
    Campo_Contacto,
    CampoExtra
)
#Serializers
from contacto.api.serializers import (
    GrupoSerializer,
    ContactoSerializar,
    CampoExtraSerializer,
    Campo_ContactoSerializer,
)
#Filters
from contacto.api.filterings import (
    GrupoFiltering,
    ContactoFiltering,
    Campo_ContactoFilterin
)

##Paginacion - clase.
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 2500


#Grupo
class GrupoViewSet(viewsets.ModelViewSet):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = GrupoFiltering


#Contacto
class ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactoSerializar
    queryset = Contacto.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ContactoFiltering

    @action(detail=False, methods=["get"])
    def grupo(self, request):
        grupo = request.query_params.get("grupo")
        
        queryset = Contacto.objects.filter(grupo=grupo)
        serializer = ContactoSerializar(queryset, many=True)

        responses = []

        contactos = serializer.data
        for contacto in contactos:
            ##Traert sus campo extras con valores
            response = {"id":contacto["id"], "nombre":contacto["nombre"], "correo":contacto["correo"]}
            querysetCampos = Campo_Contacto.objects.filter(contacto=contacto["id"])
            serializerCampo = Campo_ContactoSerializer(querysetCampos, many=True)

            for campo in serializerCampo.data:
                response[campo["campo"]] = campo["valor"]

            responses.append(response)

        return Response(responses)


#Campo Extra
class CampoExtraViewSet(viewsets.ModelViewSet):
    serializer_class = CampoExtraSerializer
    queryset = CampoExtra.objects.all()

    @action(detail=False, methods=["post"])
    def addcampo(self, request):

        campo = request.data["campo"]
        grupo = request.data["grupo"]

        #Verificar si existe elcampo y agregar al grupo
        #Creado
        queryset = CampoExtra.objects.get_or_create(nombre=campo)
        ##Anidar al grupo
        querysetGrupo = Grupo.objects.get(pk=grupo)
        serializerGrupo = GrupoSerializer(querysetGrupo)
        
        serializerGrupo.data["campos_extra"] = serializerGrupo.data["campos_extra"].append(campo)
        datos = serializerGrupo.data
        updated = GrupoSerializer(instance=querysetGrupo,data={"campos_extra": datos["campos_extra"]}, partial=True)
        response = {}
        if updated.is_valid():
            updated.save()
            response = {"campo": campo, "grupo": grupo, "estatus": "created"}
        else:
            response = {"campo": campo, "grupo": grupo, "estatus": "error"}

        return Response(response)


class Campo_ContactoViewSet(viewsets.ModelViewSet):
    serializer_class = Campo_ContactoSerializer
    queryset = Campo_Contacto.objects.all()
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = Campo_ContactoFilterin

    ##Agregar tarea para si no existe elvalor crearlo o actualizarlo
    @action(detail=False, methods=["post"])
    def newvalues(self, request):
        contacto = request.data["contacto"]
        campos = request.data["campos"]

        responses = []
        
        for campo in campos:
            try:
                queryset = Campo_Contacto.objects.get(contacto=contacto, campo=campo["campo"])
                updated = Campo_ContactoSerializer(instance=queryset,data={"valor": campo["valor"]}, partial=True)
                if updated.is_valid():
                    responses.append({"campo":campo["campo"], "estatus":"Actualizado"})
                    updated.save()
                else:
                    responses.append({"campo":campo["campo"], "estatus":updated.errors})
                
            except (ObjectDoesNotExist):
                serializerCreate = Campo_ContactoSerializer(data={"contacto": contacto, "campo": campo["campo"], "valor": campo["valor"]})
                if serializerCreate.is_valid():
                    responses.append({"campo":campo["campo"], "estatus":"Creado"})
                    serializerCreate.save()
                else:
                    responses.append({"campo":campo["campo"], "estatus":serializerCreate.errors})


        return Response(responses)

