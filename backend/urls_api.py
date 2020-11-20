from django.contrib import admin
from rest_framework.routers import DefaultRouter

from marketing.api.views import UsuarioViewSet, CuentaViewSet, ClienteViewSet,CuentaUsuarioViewSet
from contacto.api.views import (
    GrupoViewSet,
    ContactoViewSet,
    CampoExtraViewSet,
    Campo_ContactoViewSet
)
from eventos.api.views import EventoViewSet, TagsEventoViewSet, LugarEventoViewSet, OnlineEventoViewSet, ComponenteViewSet, BoletoEventoViewSet, Asistente_EventoViewSet, Boleto_AsistenteEventoViewSet, Detalles_OxxoPay_EventoViewSet, Detalles_PagoTarjeta_EventoViewSet, Donacion_Asistente_EventoViewSet, ImagenPrincipalViewSet

from emailmarketing.api.views import (
    BoletinViewSet, FechaHoraPublicacionBoletinViewSet, GrupoEnvioBoletinViewSet,
    ImagenBoletinViewSet, PlantillaBoletinViewSet, LinkBoletinViewSet, SeenContactoBoletinViewSet,
    SeenLinkBoletinViewSet, EnvioBoletinViewSet
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
router.register('tags-evento', TagsEventoViewSet, basename='tag_evento')
router.register('lugar-evento',LugarEventoViewSet,basename='lugar_evento')
router.register('online-evento',OnlineEventoViewSet,basename='online_evento')
router.register('componente',ComponenteViewSet,basename='componente')

router.register('boleto-evento', BoletoEventoViewSet, basename='boleeto_evento')
router.register('asistente-evento', Asistente_EventoViewSet, basename='asistente_evento')
router.register('boleto-asistente-evento', Boleto_AsistenteEventoViewSet, basename='boleto_asistente_evento')
router.register('detalles-oxxo-pay-evento', Detalles_OxxoPay_EventoViewSet, basename='detalles_oxxo_pay_evento')
router.register('detalles-card-pay-evento',  Detalles_PagoTarjeta_EventoViewSet, basename='detalles_card_pay_evento')
router.register('donacion_evento', Donacion_Asistente_EventoViewSet, basename='donacion_evento')
router.register('boletin', BoletinViewSet, basename='boletin')
router.register('fecha-publicacion-boletin', FechaHoraPublicacionBoletinViewSet, basename='fecha_publicacion_boletin')
router.register('grupo-envio-boletin', GrupoEnvioBoletinViewSet, basename='grupo_envio_boletin')
router.register('platilla-boletin', PlantillaBoletinViewSet, basename='platilla_boletin')
router.register('imagen-boletin', ImagenBoletinViewSet, basename='imagen_boletin')
router.register('link-boletin', LinkBoletinViewSet, basename='link_boletin')
router.register('seen-contacto-boletin', SeenContactoBoletinViewSet, basename='seen_contacto_boletin')
router.register('seen-contacto-link', SeenLinkBoletinViewSet, basename='seen_contacto_link')
router.register('envio-boletin-exitoso', EnvioBoletinViewSet, basename="envio_boletin_exitoso")

router.register('encuesta',EncuestaViewSet, basename='encuesta')
router.register('imagen-encuesta', ImagenViewSet, basename='imagen-encuesta')
router.register('encuestado', EncuestadoViewSet, basename='encuestado')
urlpatterns = router.urls
