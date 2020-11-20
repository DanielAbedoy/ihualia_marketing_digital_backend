from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from emailmarketing.api.views import SeenContactoBoletinPostView, SeenLinkBoletinPostView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls_api')),
    path('api/post/seen-contacto-boletin/', SeenContactoBoletinPostView.as_view()),
    path('api/post/seen-contacto-link/', SeenLinkBoletinPostView.as_view()),
]

