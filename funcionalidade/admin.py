from django.contrib import admin

from .models import Exame,Consulta,BancoSanguineo,Prontuario,Procedimento

# Register your models here.
admin.site.register(Exame)
admin.site.register(Consulta)
admin.site.register(BancoSanguineo)
admin.site.register(Prontuario)
admin.site.register(Procedimento)

