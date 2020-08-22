from django.contrib import admin

from eventos.models import Evento, Tags_Evento, Lugar_Evento, Online_Evento, Parrafo_Evento, Imagen_Evento, Video_Evento, Boleto_Evento, Asistente_Evento, Boleto_AsistenteEvento, Detalles_OxxoPay_Evento, Detalles_PagoTarjeta_Evento, Donacion_Asistente_Evento

# Register your models here.
admin.site.register(Evento)
admin.site.register(Tags_Evento)
admin.site.register(Lugar_Evento)
admin.site.register(Online_Evento)
admin.site.register(Parrafo_Evento)
admin.site.register(Imagen_Evento)
admin.site.register(Video_Evento)
admin.site.register(Boleto_Evento)
admin.site.register(Asistente_Evento)
admin.site.register(Boleto_AsistenteEvento)
admin.site.register(Detalles_OxxoPay_Evento)
admin.site.register(Detalles_PagoTarjeta_Evento)
admin.site.register(Donacion_Asistente_Evento)

