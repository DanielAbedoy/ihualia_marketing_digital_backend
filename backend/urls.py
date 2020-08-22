from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contacto.api.views import GrupoPostView, GrupoContacto_PostView, CampoExtra_Grupo_PostView, Campo_Contacto_PostView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls_api')),    
    path('api/post/grupo/', GrupoPostView.as_view()),
    path('api/post/grupo-contacto/', GrupoContacto_PostView.as_view()),
    path('api/post/campo-extra-grupo/', CampoExtra_Grupo_PostView.as_view()),
    path('api/post/campo-contacto/', Campo_Contacto_PostView.as_view()) 
]

