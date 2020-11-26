from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import pagination
from django_filters import rest_framework as filters
import sys

from eventos.api.serializers import EventoSerializer, Asistente_EventoSerializer, ImagenPrincipalSerializer

from eventos.models import Evento, Asistente_Evento, ImagenPrincipal

from eventos.api.filterings import  EventoFiltering, AsistenteEventoFiltering

class EventoViewSet(ModelViewSet):
  serializer_class = EventoSerializer
  queryset = Evento.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = EventoFiltering

  @action(detail=False, methods=["get"])
  def info(self, request):

    cuenta = request.query_params.get("cuenta")

    queryset = Evento.objects.filter(id_cuenta=cuenta)
    serializer = EventoSerializer(queryset, many=True)
    
    resp = []
    for evento in serializer.data:
      resp.append({"id": evento["id"], "nombre":evento["nombre"],"tipo": evento["tipo"], "categoria": evento["categoria"], "estatus": evento["estatus"], "url":evento["url"]})

    return Response(resp)

  @action(detail=True, methods=["get"])
  def tocontinue(self, request, pk=None):

    queryset = Evento.objects.get(id=pk)
    serializer = EventoSerializer(queryset)

    e = serializer.data
    r = {"id": e["id"], "etiquetas": e["etiquetas"], "ubicacion": e["ubicacion"],"componentes": e["componentes"],"boletos": e["boletos"],"nombre": e["nombre"],"tipo": e["tipo"],
        "categoria": e["categoria"],"sub_categoria": e["sub_categoria"],"fecha_hora_inicio": e["fecha_hora_inicio"],"fecha_hora_fin": e["fecha_hora_fin"],"zona_horaria": e["zona_horaria"],"resumen": e["resumen"],"estatus": e["estatus"],"imagen": e["imagen"],"url": e["url"], "id_cuenta": e["id_cuenta"]
      }

    return Response(r)
    

class Asistente_EventoViewSet(ModelViewSet):
  serializer_class = Asistente_EventoSerializer
  queryset = Asistente_Evento.objects.all()
  
  @action(detail=False, methods=["post"])
  def add(self, request):

    infoAsistente = request.data["infoPrincipal"]#correo, nombre, telefono, metodo_pago, monto_total, estatus_pago
    boletos = request.data["boletos"] # cantidad, id_asistencia, id_boleto
    donacion = request.data["donacion"]  # monto, id_asistencia
    detalles = request.data["detalles"]

    response =[]
    serializer = Asistente_EventoSerializer(data={"correo":infoAsistente["correo"],"nombre":infoAsistente["nombre"], "telefono":infoAsistente["telefono"],"metodo_pago":infoAsistente["metodo_pago"],"monto_total":infoAsistente["monto_total"],"estatus_pago":infoAsistente["estatus_pago"], "id_evento": infoAsistente["evento"] })

    ##Agregando asistente
    if serializer.is_valid():
      asistente = serializer.save()
      response.append({"Asistente":"creado"})
      id_asistencia = asistente.id
      boletosResp=[]
      #Agregando boletos
      
      for boleto in boletos:
        serailizerBoleto = Boleto_AsistenteEventoSerializer(data={"cantidad":boleto["cantidad"], "id_asistencia":id_asistencia,"id_boleto":boleto["id"]})
        if serailizerBoleto.is_valid():
          serailizerBoleto.save()
          boletosResp.append({"boleto": boleto["id"], "estatus": "agregado"})
        else:
          boletosResp.append({"boleto": boleto["id"], "erro":serailizerBoleto.errors })
      
      response.append({"boletos": boletosResp})
      ##Donacion
      if donacion["are"]:
        serializerDonacion = Donacion_Asistente_EventoSerializer(data={"monto":donacion["monto"],"id_asistencia":id_asistencia})
        if serializerDonacion.is_valid():
          serializerDonacion.save()
          response.append({"donacion":"agregada" })

      #Detalles
      if detalles["are"]:
        data = detalles["data"]
        if data["tipo"] == "oxxo":
          serializerOxxo = Detalles_OxxoPay_EventoSerializer(data={"numero_referencia":data["referencia"],"id_asistencia":id_asistencia})
          if serializerOxxo.is_valid():
            serializerOxxo.save()
            response.append({"detalles":"agregados"})
        elif data["tipo"] == "card":
          serializerCard = Detalles_OxxoPay_EventoSerializer(data={"id_pago":data["id_pago"],"id_orden":data["id_orden"], "id_asistencia":id_asistencia})
          if serializerCard.is_valid():
            serializerCard.save()
            response.append({"detalles":"agregados"})

    else:
      response.append({"error":serializer.errors, "estatus":"error"})
      
    return Response(response)


class ImagenPrincipalViewSet(ModelViewSet):
  serializer_class = ImagenPrincipalSerializer
  queryset = ImagenPrincipal.objects.all()