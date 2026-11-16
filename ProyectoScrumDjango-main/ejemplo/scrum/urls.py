from . import views
from django.urls import path

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path("crearTarea/", views.crear_tarea , name="crear_tarea"),

]
'''
    path('listarTareas/', views.listar_tareas, name='listarTareas'),
    path('listarTarea/<int:id>', views.listar_tarea, name='listarTarea'),
    path('listarTareaMejorada/<int:id>', views.listar_tarea_mejorado, name='listarTareaMejorada'),
    path('listarTareasCompletas/', views.listar_tareas_completas, name='listarTareasCompletas'),'''