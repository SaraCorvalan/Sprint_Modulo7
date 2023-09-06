
from django.contrib import admin
from django.urls import path
from tareas.views import tareas
from tareas.views import *
from django.contrib.auth import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', tareas, name = 'index'),
    path('registro_tareas/login/', tareas, name = 'index'),
    
    path('administra_tareas_estado/login/', tareas, name = 'index'),
    path('administra_tareas_tarea/login/', tareas, name = 'index'),
    path('administra_tareas_vencimiento/login/', tareas, name = 'index'),
    path('completa_tareas/login/', tareas, name = 'index'),
    path('enProgreso_tareas/login/', tareas, name = 'index'),
    path('enProgreso_tareas/login/',tareas_pendientes, name= 'index'),
    path('',tareas_pendientes, name= 'index'),
    
    path('resumen_tareas/', resumen_tareas, name='resumen_tareas'),
    path('enProgreso_tareas/',tareas_pendientes, name= 'index'),
    path('registro_tareas/', formularioRegistroTareas, name = 'registro_tareas'),
    path('administra_tareas_estado/', administraTareasEstado, name = 'administra_tareas_estado'),
    path('administra_tareas_tarea/', administraTareasTarea, name = 'administra_tareas_tarea'),
    path('administra_tareas_vencimiento/', administraTareasVencimiento, name = 'administra_tareas_vencimiento'),

    path('modifica_tareas/<id>/', modificaTareas, name="modifica_tareas"),
    path('elimina_tareas/<id>/', eliminaTareas, name = 'elimina_tareas'),
    path('completa_tareas/<id>/', completaTareas, name = 'completa_tareas'),
    path('enProgreso_tareas/<id>/', enProgresoTareas, name = 'enProgreso_tareas'),

    path('login/', user_login, name = 'login'),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
]

