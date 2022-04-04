from django.contrib import admin
from .models import Medico, User
from django.contrib.auth.admin import UserAdmin

ADICIONAR_CAMPOS = list(UserAdmin.fieldsets)
ADICIONAR_CAMPOS.append(
    ('Tipo de User', {'fields': ('user_type',)})
)
ADICIONAR_CAMPOS.append(
    ('Tipo Sanguineo', {'fields': ('blood_type',)})
)
ADICIONAR_CAMPOS.append(
    ('Cadastro de Pessoa Física', {'fields': ('cpf',)})
)

UserAdmin.fieldsets = tuple(ADICIONAR_CAMPOS)

# Register your models here.
admin.site.register(Medico)
admin.site.register(User, UserAdmin)
