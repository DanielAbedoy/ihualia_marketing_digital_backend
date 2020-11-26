from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from encuestas.models import Imagen, Encuesta, Encuestado
from encuestas.api.serializers import ImagenSerializer, EncuestaSerializer, EncuestadoSerializer
from encuestas.api.filterings import EncuestFiltering

class ImagenViewSet(ModelViewSet):

  serializer_class = ImagenSerializer
  queryset = Imagen.objects.all()

class EncuestaViewSet(ModelViewSet):
  serializer_class = EncuestaSerializer
  queryset = Encuesta.objects.all()
  filter_backends = [filters.DjangoFilterBackend]
  filterset_class = EncuestFiltering

  @action(detail=False, methods=["get"])
  def getinfo(self, request):
    
    cuenta = request.query_params.get("cuenta")

    queryset = Encuesta.objects.filter(cuenta=cuenta)
    serializer = EncuestaSerializer(queryset, many=True)

    encuestas = []
    for e in serializer.data:
      encuestas.append({"id":e["id"], "nombre":e["nombre"], "estatus":e["estatus"], "url":e["url"]})
    return Response(encuestas)

  @action(detail=False, methods=["get"])
  def getinfotoshow(self, request):
    url = request.query_params.get("url")

    queryset = Encuesta.objects.get(url=url)
    serializer = EncuestaSerializer(queryset)

    e = serializer.data
    resp = {"id":e["id"], "nombre":e["nombre"], "presentacion":e["presentacion"], "instrucciones":e["instrucciones"],"imagen":e["imagen"],"anonima":e["anonima"],"ponderacion":e["ponderacion"],"paginacion":e["paginacion"], "preguntas_json":e["preguntas_json"],"despedida":e["despedida"],"estatus":e["estatus"],"url":e["url"]}
    return Response(resp)



class EncuestadoViewSet(ModelViewSet):

  serializer_class = EncuestadoSerializer
  queryset = Encuestado.objects.all()

  


