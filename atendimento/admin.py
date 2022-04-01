from django.contrib import admin
from .models import Pet
from .models import Responsavel
from .models import Atendimento


admin.site.register(Pet)
admin.site.register(Responsavel)
admin.site.register(Atendimento)