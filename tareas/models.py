from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

categorias = (
    ("1", "Trabajo"),
    ("2", "Hogar"),
    ("3", "Estudio"),
    ("4", "Otras categorías"),
)

estados = (
    ("1", "Pendiente"),
    ("2", "En progreso"),
    ("3", "Completada"),
)
class Prioridad(models.Model):
    PRIORIDAD_CHOICES = (
        ('1', 'Alta'),
        ('2', 'Mediana'),
        ('3', 'Baja'),
    )
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='baja')
    

    def __str__(self):
        return self.prioridad
class registroTareas(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    titulo_tarea = models.CharField(max_length=50, verbose_name="Título de tarea")
    descripcion_tarea = models.CharField(max_length=80, verbose_name="Descripción de tarea")    
    fecha_vencimiento_tarea = models.DateField(default=timezone.now, verbose_name="Fecha vencimiento tarea (dd-mm-yyyy)")
    categoria_tarea = models.CharField(max_length=1, choices=categorias, default='1', verbose_name="Categoria tarea") 
    estado_tarea = models.CharField(max_length=1, choices=estados, default='1', verbose_name="Estado de tarea")
    observaciones_tarea = models.TextField(max_length=300)
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE,  default='1',related_name='tareas_asignadas', null=True, blank=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, default='1', related_name='prioridad_tareas', null=True, blank=True)
            
    def __str__(self):
        return "Id: %s, Nombre Tarea: %s, Descripción tarea: %s,  Vencimiento tarea: %s, Categoria: %s, Estado: %s, Observaciones: %s" %(
            self.id_tarea, 
            self.titulo_tarea, 
            self.descripcion_tarea, 
            self.fecha_vencimiento_tarea, 
            self.categoria_tarea, 
            self.estado_tarea,
            self.observaciones_tarea,
            self.asignado_a,
            self.prioridad)
    



