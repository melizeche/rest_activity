from django.contrib import admin

from .models import Actividad, Tipo, Origen, Imagen
# Register your models here.

admin.site.register(Actividad)
admin.site.register(Tipo)
admin.site.register(Origen)
admin.site.register(Imagen)
