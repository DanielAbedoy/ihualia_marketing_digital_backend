from django.contrib import admin
from rest_framework.routers import DefaultRouter

from marketing.api.views import UsuarioViewSet, CuentaViewSet, ClienteViewSet, Usuario_Cuenta_ViewSet
from contacto.api.views import (
    GrupoViewSet,
    ContactoViewSet,
    GrupoContactoViewSet,
    CampoExtraViewSet,
    CampoExtra_GrupoViewSet,
    Campo_ContactoViewSet
)
from eventos.api.views import EventoViewSet, TagsEventoViewSet, LugarEventoViewSet, OnlineEventoViewSet, ParrafoEventoViewSet, ImagenEventoViewSet, VideoEventoViewSet, BoletoEventoViewSet, Asistente_EventoViewSet, Boleto_AsistenteEventoViewSet, Detalles_OxxoPay_EventoViewSet, Detalles_PagoTarjeta_EventoViewSet, Donacion_Asistente_EventoViewSet

from emailmarketing.api.views import (
    BoletinViewSet, FechaHoraPublicacionBoletinViewSet, GrupoEnvioBoletinViewSet,
    ImagenBoletinViewSet, PlantillaBoletinViewSet, LinkBoletinViewSet, SeenContactoBoletinViewSet,
    SeenLinkBoletinViewSet, EnvioBoletinViewSet
)

router = DefaultRouter()
router.register('cliente', ClienteViewSet, basename='cliente')
router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('cuenta', CuentaViewSet, basename='cuenta')
router.register('usuario-cuenta', Usuario_Cuenta_ViewSet, basename='usuario_cuenta')
router.register('contacto', ContactoViewSet, basename='contacto')
router.register('grupo', GrupoViewSet, basename='grupo')
router.register('grupo-contacto', GrupoContactoViewSet, basename='grupo_contacto')
router.register('campo-extra', CampoExtraViewSet, basename='campo_extra')
router.register('campo-extra-grupo', CampoExtra_GrupoViewSet, basename='campoextra_grupo')
router.register('campo-contacto', Campo_ContactoViewSet, basename='campo_contacto')
router.register('evento', EventoViewSet, basename='evento')
router.register('tags-evento', TagsEventoViewSet, basename='tag_evento')
router.register('lugar-evento',LugarEventoViewSet,basename='lugar_evento')
router.register('online-evento',OnlineEventoViewSet,basename='online_evento')
router.register('parrafo-evento',ParrafoEventoViewSet,basename='parrafo_evento')
router.register('imagen-evento',ImagenEventoViewSet,basename='imagen_evento')
router.register('video-evento',VideoEventoViewSet,basename='video_evento')
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
router.register('envio-boletin-exitoso', EnvioBoletinViewSet, basename="envio_boletin_exitoso" )
urlpatterns = router.urls
