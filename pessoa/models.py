from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
TIPO_SANGUE = (
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

LISTA_ESPECIALIDADES = (
    ('Neurologista', 'Neurologista'),
    ('Cardiologista', 'Cardiologista'),
    ('Pediatra', 'Pediatra'),
    ('Ortopedista', 'Ortopedista'),
    ('Psiquiatra', 'Psiquiatra'),
    ('Oftalmologista', 'Oftalmologista'),
    ('Dermatologista', 'Dermatologista'),
    ('Geriatra', 'Geriatra'),
    ('Ginecologista', 'Ginecologista'),
    ('Psicólogo', 'Psicólogo'),
    ('Urologista', 'Urologista'),
    ('Radioterapeuta', 'Radioterapeuta'),
    ('Otorrinolaringologista', 'Otorrinolaringologista'),
    ('Clínico Geral', 'Clínico Geral'),
)

USER_TYPE = (
    ('Médico', 'Médico'),
    ('Paciente', 'Paciente'),
    ('Administrador', 'Administrador'),
)

UF = (
    ('MG', 'MG'),
    ("AC", "AC"),
    ("AL", "AL"),
    ("AP", "AP"),
    ("AM", "AM"),
    ("BA", "BA",),
    ("CE", "CE",),
    ("DF", "DF",),
    ("ES", "ES",),
    ("GO", "GO",),
    ("MA", "MA",),
    ("MT", "MT",),
    ("MS", "MS",),
    ("PA", "PA",),
    ("PB", "PB",),
    ("PR", "PR",),
    ("PE", "PE",),
    ("PI", "PI",),
    ("RJ", "RJ",),
    ("RN", "RN",),
    ("RS", "RS",),
    ("RO", "RO",),
    ("RR", "RO",),
    ("SC", "SC",),
    ("SP", "SP",),
    ("SE", "SE",),
    ("TO", "TO",),
)


class User(AbstractUser):
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=16, null=True)
    blood_type = models.CharField(max_length=3, choices=TIPO_SANGUE, null=True)
    user_type = models.CharField(max_length=15, choices=USER_TYPE)


class Medico(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    crm = models.CharField(max_length=10)
    uf = models.CharField(max_length=2, choices=UF)
    specialty = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.user.username
