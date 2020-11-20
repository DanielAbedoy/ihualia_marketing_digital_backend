from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, CuentaViewSet, ClienteViewSet


router = DefaultRouter()
router.register('cliente', ClienteViewSet, basename='cliente')
router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('cuenta', CuentaViewSet, basename='cuenta')
urlpatterns = router.urls
