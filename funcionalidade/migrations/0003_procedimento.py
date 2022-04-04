# Generated by Django 4.0.3 on 2022-03-12 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_alter_medico_specialty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionalidade', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Cirurgia Plástica', 'Cirurgia Plástica'), ('Retirada de tumor', 'Retirada de tumor'), ('Retirada de sinal', 'Retirada de sinal'), ('Fisioterapia', 'Fisioterapia'), ('Hemodiálise', 'Hemodiálise'), ('Cirurgia Bariátrica', 'Cirurgia Bariátrica'), ('Amputação de Membro', 'Amputação de Membro'), ('Imobilização de membro', 'Imobilização de membro'), ('Cirurgia Auditiva', 'Cirurgia Auditiva'), ('Cirurgia Ocular', 'Cirurgia Ocular')], max_length=40)),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.medico')),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]