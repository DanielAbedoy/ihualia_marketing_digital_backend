from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    GrupoViewSet,
    ContactoViewSet,
    GrupoContactoViewSet,
    CampoExtraViewSet,
    CampoExtra_GrupoViewSet,
    Campo_ContactoViewSet
)

router = DefaultRouter()
router.register('contacto', ContactoViewSet, basename='contacto')
router.register('grupo', GrupoViewSet, basename='grupo')
router.register('grupo-contacto', GrupoContactoViewSet, basename='grupocontacto')
router.register('campo-extra', CampoExtraViewSet, basename='campoextra')
router.register('campo-extra-grupo', CampoExtra_GrupoViewSet, basename='campoextragrupo')
router.register('campo-contacto', Campo_ContactoViewSet, basename='campocontacto')
urlpatterns = router.urls

