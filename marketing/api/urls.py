from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, CuentaViewSet, ClienteViewSet, Usuario_Cuenta_ViewSet


router = DefaultRouter()
router.register('cliente', ClienteViewSet, basename='cliente')
router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('cuenta', CuentaViewSet, basename='cuenta')
router.register('usuario-cuenta', Usuario_Cuenta_ViewSet, basename='usuario_cuenta')
urlpatterns = router.urls
