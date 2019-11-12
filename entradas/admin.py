from django.contrib import admin
from .  models import Artistas, Genero, Tickets, Conciertos, Suscriptor
# Register your models here.

admin.site.register(Artistas)
admin.site.register(Genero)
admin.site.register(Tickets)
admin.site.register(Conciertos)
admin.site.register(Suscriptor)
