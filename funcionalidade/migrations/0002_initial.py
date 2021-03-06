# Generated by Django 4.0.2 on 2022-03-12 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionalidade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prontuario',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.medico'),
        ),
        migrations.AddField(
            model_name='prontuario',
            name='pacient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exame',
            name='pacient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consulta',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='pacient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
