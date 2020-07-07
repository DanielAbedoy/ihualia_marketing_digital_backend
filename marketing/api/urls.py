from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, CuentaViewSet


router = DefaultRouter()
router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('cuenta', CuentaViewSet, basename='usuario')
urlpatterns = router.urls
