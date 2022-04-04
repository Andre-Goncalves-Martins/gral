from django.db import models
from pessoa.models import User, Medico, TIPO_SANGUE
from django.utils import timezone

TIPO_EXAME = (
    ('Hemograma', 'Hemograma'),
    ('Colesterol e Triglicerídeos', 'Colesterol e Triglicerídeos'),
    ('Mamografia', 'Mamografia'),
    ('Ressonância Magnética', 'Ressonância Magnética'),
    ('Tomografia', 'Tomografia'),
    ('Ultra-sonografia', 'Ultra-sonografia'),
    ('Biópsia', 'Biópsia'),
    ('Colonoscopia', 'Colonoscopia'),
    ('Raio X', 'Raio X'),
    ('Laringoscopia', 'Laringoscopia'),
    ('Cateterismo', 'Cateterismo'),
    ('Urografia', 'Urografia'),
    ('Teste do Pezinho', 'Teste do Pezinho'),
    ('Endoscopia', 'Endoscopia'),
    ('Eletroencefalografia', 'Eletroencefalografia'),
    ('Exame de Fezes', 'Exame de Fezes'),
    ('Diagnostico Pré-Natal', 'Diagnostico Pré-Natal')
)

ESTADOS_EXAMES = (
    ('Em Andamento', 'Em Andamento'),
    ('Pronto', 'Pronto'),
)

LISTA_PROCEDIMENTOS = (
    ('Cirurgia Plástica', 'Cirurgia Plástica'),
    ('Retirada de tumor', 'Retirada de tumor'),
    ('Retirada de sinal', 'Retirada de sinal'),
    ('Fisioterapia', 'Fisioterapia'),
    ('Hemodiálise', 'Hemodiálise'),
    ('Cirurgia Bariátrica', 'Cirurgia Bariátrica'),
    ('Amputação de Membro', 'Amputação de Membro'),
    ('Imobilização de membro', 'Imobilização de membro'),
    ('Cirurgia Auditiva', 'Cirurgia Auditiva'),
    ('Cirurgia Ocular', 'Cirurgia Ocular'),
)

LISTA_HORARIOS = (
    ('8:00', '8:00'),
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
)

LISTA_DATAS = (
    ('04 DE ABRIL', '04 DE ABRIL'),
    ('05 DE ABRIL', '05 DE ABRIL'),
    ('06 DE ABRIL', '06 DE ABRIL'),
    ('07 DE ABRIL', '07 DE ABRIL'),
    ('08 DE ABRIL', '08 DE ABRIL'),
)


# Create your models here.


class Exame(models.Model):
    state = models.CharField(choices=ESTADOS_EXAMES,
                             max_length=12, default='Em Andamento')
    exam_type = models.CharField(max_length=30, choices=TIPO_EXAME)
    exam_date = models.CharField(max_length=12, choices=LISTA_DATAS)
    exam_hour = models.CharField(max_length=5, choices=LISTA_HORARIOS)
    exam_result = models.CharField(
        max_length=30, default='Ainda Não Concluido')
    pacient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pacient.username


class Consulta(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    consult_date = models.CharField(max_length=12, choices=LISTA_DATAS)
    consult_hour = models.CharField(max_length=5, choices=LISTA_HORARIOS)
    doctor = models.ForeignKey(Medico, on_delete=models.CASCADE)
    pacient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.date_time}'


class BancoSanguineo(models.Model):
    volum = models.FloatField(max_length=5)  # Em Litros
    blood_type = models.CharField(max_length=10, choices=TIPO_SANGUE)
    donation_date = models.CharField(max_length=12, choices=LISTA_DATAS)
    donation_hour = models.CharField(max_length=5, choices=LISTA_HORARIOS)

    def __str__(self) -> str:
        return f'{self.donation_date}'


class Prontuario(models.Model):
    medical_records = models.TextField()
    date = models.CharField(max_length=12, choices=LISTA_DATAS)
    pacient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return self.pacient.username


class Procedimento(models.Model):
    type = models.CharField(choices=LISTA_PROCEDIMENTOS, max_length=40)
    date = models.CharField(max_length=12, choices=LISTA_DATAS)
    pacient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return self.pacient.username

# Procedimento
