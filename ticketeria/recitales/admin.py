from django.contrib import admin
from .models import Establecimiento, Recital, Usuario, Reserva

admin.site.register(Establecimiento)
admin.site.register(Recital)
admin.site.register(Usuario)
admin.site.register(Reserva)