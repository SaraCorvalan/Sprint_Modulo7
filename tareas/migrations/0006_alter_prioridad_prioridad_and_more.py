# Generated by Django 4.2.3 on 2023-09-06 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareas', '0005_registrotareas_prioridad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prioridad',
            name='prioridad',
            field=models.CharField(choices=[('1', 'Alta'), ('2', 'Mediana'), ('3', 'Baja')], default='baja', max_length=10),
        ),
        migrations.AlterField(
            model_name='registrotareas',
            name='asignado_a',
            field=models.ForeignKey(blank=True, default='asignar', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tareas_asignadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registrotareas',
            name='prioridad',
            field=models.ForeignKey(blank=True, default='baja', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prioridad_tareas', to='tareas.prioridad'),
        ),
    ]
