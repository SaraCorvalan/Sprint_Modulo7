# Generated by Django 4.2.4 on 2023-08-23 01:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registroTareas',
            fields=[
                ('id_tarea', models.CharField(default='100', max_length=3, primary_key=True, serialize=False)),
                ('titulo_tarea', models.CharField(max_length=50, verbose_name='Título de tarea')),
                ('descripcion_tarea', models.CharField(max_length=80, verbose_name='Descripción de tarea')),
                ('fecha_vencimiento_tarea', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha vencimiento tarea (dd-mm-yyyy)')),
                ('categoria_tarea', models.CharField(choices=[('1', 'Trabajo'), ('2', 'Hogar'), ('3', 'Estudio'), ('4', 'Otras categorías')], default='1', max_length=1, verbose_name='Categoria tarea')),
                ('estado_tarea', models.CharField(choices=[('1', 'Pendiente'), ('2', 'En progreso'), ('3', 'Completada')], default='1', max_length=1, verbose_name='Estado de tarea')),
                ('observaciones_tarea', models.TextField(max_length=300)),
            ],
        ),
    ]
