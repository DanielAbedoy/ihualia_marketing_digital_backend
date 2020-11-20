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

from eventos.api.serializers import EventoSerializer, TagsEventoSerializer, LugarEventoSerializer, ComponenteSerializer, OnlineEventoSerializer, BoletoEventoSerializer, Asistente_EventoSerializer, Boleto_AsistenteEventoSerializer, Detalles_OxxoPay_EventoSerializer, Detalles_PagoTarjeta_EventoSerializer, Donacion_Asistente_EventoSerializer, ImagenPrincipalSerializer

from eventos.models import Evento, Tags_Evento, Lugar_Evento, Online_Evento, Componente, Boleto_Evento, Asistente_Evento, Boleto_AsistenteEvento, Detalles_PagoTarjeta_Evento, Detalles_OxxoPay_Evento, Donacion_Asistente_Evento, ImagenPrincipal

from eventos.api.filterings import TagsEventoFiltering, LugarEventoFiltering, OnlineEventoFiltering, BoletoEventoFiltering, Boleto_Asistente_EventoFiltering, EventoFiltering, AsistenteEventoFiltering, DonacionEventoFiltering

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
      resp.append({"id": evento["id"], "nombre":evento["nombre"],"tipo": evento["tipo"], "categoria": evento["categoria"], "estatus": evento["estatus"]})

    return Response(resp)

  @action(detail=True, methods=["get"])
  def tocontinue(self, request, pk=None):

    queryset = Evento.objects.get(id=pk)
    serializer = EventoSerializer(queryset)

    e = serializer.data
    r = {"id": e["id"], "etiquetas": e["etiquetas"], "lugar": e["lugar"],"sitio": e["sitio"],"componentes": e["componentes"],"boletos": e["boletos"],"nombre": e["nombre"],"tipo": e["tipo"],
        "categoria": e["categoria"],"sub_categoria": e["sub_categoria"],"tipo_ubicacion": e["tipo_ubicacion"],"fecha_hora_inicio": e["fecha_hora_inicio"],"fecha_hora_fin": e["fecha_hora_fin"],"zona_horaria": e["zona_horaria"],"resumen": e["resumen"],"estatus": e["estatus"],"imagen": e["imagen"],"url": e["url"], "id_cuenta": e["id_cuenta"]
      }

    return Response(r)
    
    


  
class TagsEventoViewSet(ModelViewSet):
  serializer_class = TagsEventoSerializer
  queryset = Tags_Evento.objects.all()
  
  @action(detail=False, methods=["post"])
  def newvalues(self, request):

    evento = request.data["evento"]
    etiquetas = request.data["etiquetas"]

    queryset = Tags_Evento.objects.filter(id_evento= evento)
    queryset.delete()
 
    responses = []
    for etiqueta in etiquetas:
      serializerNew = TagsEventoSerializer(data={"id_evento": evento, "palabra": etiqueta})
      if serializerNew.is_valid():
        responses.append({"etiqueta": etiqueta, "status":"Created"})
        serializerNew.save()
      else:
        responses.append({"etiqueta": etiqueta, "status":"Error"})
    
    return Response(responses)



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

class ComponenteViewSet(ModelViewSet):
  serializer_class = ComponenteSerializer
  queryset = Componente.objects.all()

  @action(detail=False, methods=["post"])
  def newvalues(self, request):
    
    evento = request.data["evento"]
    componentes = request.data["componentes"]

    queryset = Componente.objects.filter(id_evento= evento)
    queryset.delete()

    responses = []
    for componente in componentes:
      serializerNew = ComponenteSerializer(data={"id_evento": evento, "contenido": componente["contenido"], "posicion":componente["posicion"],"tipo":componente["tipo"] })
      if serializerNew.is_valid():
        responses.append({"componente": componente["tipo"], "status":"Created"})
        serializerNew.save()
      else:
        responses.append({"componente": componente["tipo"], "status":"Error"})
    
    return Response(responses)


class BoletoEventoViewSet(ModelViewSet):
  serializer_class = BoletoEventoSerializer
  queryset = Boleto_Evento.objects.all()

  @action(detail=False, methods=["post"])
  def newvalues(self, request):
    
    evento = request.data["evento"]
    boletos = request.data["boletos"]

    queryset = Boleto_Evento.objects.filter(id_evento= evento)
    queryset.delete()

    responses = []
    for boleto in boletos:
      serializerNew = BoletoEventoSerializer(data={"id_evento": evento, "tipo":boleto["tipo"], "nombre":boleto["nombre"], "cantida_total":boleto["cantidad_total"], "precio":boleto["precio"], "descripcion":boleto["descripcion"],"cantidad_minima":boleto["cantidad_minima"], "cantidad_maxima":boleto["cantidad_maxima"],"canal_ventas":boleto["canal_ventas"] })
      if serializerNew.is_valid():
        responses.append({"boleto": boleto["nombre"], "status":"Created"})
        serializerNew.save()
      else:
        print(serializerNew.errors)
        responses.append({"boleto": boleto["nombre"], "status":"Error"})
    
    return Response(responses)


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


class Boleto_AsistenteEventoViewSet(ModelViewSet):
  serializer_class = Boleto_AsistenteEventoSerializer
  queryset = Boleto_AsistenteEvento.objects.all()
  
  @action(detail=False, methods=["post"])
  def vendidos(self, request):

    boletos = request.data["boletos"]

    responses = []
    for boleto in boletos:
      queryset = Boleto_AsistenteEvento.objects.filter(id_boleto=boleto)
      serializer = Boleto_AsistenteEventoSerializer(queryset, many=True)
      cantidad = 0
      for c in serializer.data:
        cantidad += int(c["cantidad"])

      responses.append({"boleto": boleto, "vendidos": cantidad})
      
    

    return Response(responses)

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