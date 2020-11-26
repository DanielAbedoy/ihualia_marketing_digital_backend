from django.contrib import admin

from emailmarketing.models import (
  Boletin,
  ImagenBoletin,  SeenContactoBoletin,
  SeenLinkBoletin,
)

# Register your models here.
admin.site.register(Boletin)
admin.site.register(ImagenBoletin)
admin.site.register(SeenContactoBoletin)
admin.site.register(SeenLinkBoletin)
