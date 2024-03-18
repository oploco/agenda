from django.contrib import admin

from .models import Contacto
from .models import Telefono


# Register your models here.
admin.site.register(Contacto)
admin.site.register(Telefono)