from django.contrib import admin
from rest_framework.routers import DefaultRouter

from marketing.api.views import UsuarioViewSet, CuentaViewSet, ClienteViewSet,CuentaUsuarioViewSet
from contacto.api.views import (
    GrupoViewSet,
    ContactoViewSet,
    CampoExtraViewSet,
    Campo_ContactoViewSet
)
from eventos.api.views import EventoViewSet, Asistente_EventoViewSet, ImagenPrincipalViewSet

from emailmarketing.api.views import (
    BoletinViewSet,  
    ImagenBoletinViewSet,   SeenContactoBoletinViewSet,
    SeenLinkBoletinViewSet
)

from encuestas.api.views import ImagenViewSet, EncuestaViewSet, EncuestadoViewSet

router = DefaultRouter()
router.register('cliente', ClienteViewSet, basename='cliente')
router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('cuenta', CuentaViewSet, basename='cuenta')
router.register('cuentausuario', CuentaUsuarioViewSet, basename='cuentausuario')


router.register('contacto', ContactoViewSet, basename='contacto')
router.register('grupo', GrupoViewSet, basename='grupo')
router.register('campo-extra', CampoExtraViewSet, basename='campo_extra')
router.register('campo-contacto', Campo_ContactoViewSet, basename='campo_contacto')


router.register('evento', EventoViewSet, basename='evento')
router.register('imagen-ev', ImagenPrincipalViewSet, basename='imagen_p_evento')
router.register('asistente-evento', Asistente_EventoViewSet, basename='asistente_evento')


router.register('boletin', BoletinViewSet, basename='boletin')
router.register('imagen-boletin', ImagenBoletinViewSet, basename='imagen_boletin')
router.register('seen-contacto-boletin', SeenContactoBoletinViewSet, basename='seen_contacto_boletin')
router.register('seen-contacto-link', SeenLinkBoletinViewSet, basename='seen_contacto_link')

router.register('encuesta',EncuestaViewSet, basename='encuesta')
router.register('imagen-encuesta', ImagenViewSet, basename='imagen-encuesta')
router.register('encuestado', EncuestadoViewSet, basename='encuestado')
urlpatterns = router.urls
