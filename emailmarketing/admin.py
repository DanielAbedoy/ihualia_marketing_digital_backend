from django.contrib import admin

from emailmarketing.models import (
  Boletin, FechaHoraPublicacionBoletin, GrupoEnvioBoletin,
  ImagenBoletin, LinkBoletin, PlantillaBoletin, SeenContactoBoletin,
  SeenLinkBoletin, EnvioBoletin
)

# Register your models here.
admin.site.register(Boletin)
admin.site.register(FechaHoraPublicacionBoletin)
admin.site.register(GrupoEnvioBoletin)
admin.site.register(ImagenBoletin)
admin.site.register(LinkBoletin)
admin.site.register(PlantillaBoletin)
admin.site.register(SeenContactoBoletin)
admin.site.register(SeenLinkBoletin)
admin.site.register(EnvioBoletin)