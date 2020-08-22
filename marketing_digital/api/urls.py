from django.urls import path
from rest_framework.routers import DefaultRouter

from marketing_digital.api.views import (
    UsuarioViewSet, CuentaViewSet, ClienteViewSet, Usuario_Cuenta_ViewSet,
    GrupoViewSet,
    ContactoViewSet,
    GrupoContactoViewSet,
    CampoExtraViewSet,
    CampoExtra_GrupoViewSet,
    Campo_ContactoViewSet,
    GrupoPostView,GrupoContacto_PostView,CampoExtra_Grupo_PostView, Campo_Contacto_PostView,
    
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
router.register('cliente', ClienteViewSet, basename='cliente')
router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('cuenta', CuentaViewSet, basename='cuenta')
router.register('usuario-cuenta', Usuario_Cuenta_ViewSet, basename='usuario_cuenta')
#router.register('post/grupo/', GrupoPostView.as_view(), basename='post-grupo')

""" path('api/post/grupo/', GrupoPostView.as_view()),
    path('api/post/grupo-contacto/', GrupoContacto_PostView.as_view()),
    path('api/post/campo-extra-grupo/', CampoExtra_Grupo_PostView.as_view()),
    path('api/post/campo-contacto/', Campo_Contacto_PostView.as_view())
 """
urlpatterns = router.urls