from django.contrib import admin

from tareas.models import registroTareas

class TareasAdmin(admin.ModelAdmin):
    list_display = ('id_tarea', 'titulo_tarea', 'descripcion_tarea', 'fecha_vencimiento_tarea', 'categoria_tarea', 'estado_tarea')
    
admin.site.register(registroTareas, TareasAdmin)