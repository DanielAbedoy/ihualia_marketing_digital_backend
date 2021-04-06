from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from newsletter_auth.views import login_viw, refresh_token_view
from marketing.api.views import createFirst

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls_api')),
    path('newsletter-auth', login_viw, name="auth"),
    path('newsletter-refresh-auth', refresh_token_view, name="refresh-auth" ),
    path('create-cliente', createFirst, name="create-cliente"),

]

