from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'), # Tu ruta de la Unidad 1
    
    # Nuevas rutas de la Unidad 2
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/eliminar/<int:id>/', views.baja_paciente, name='baja_paciente'),
]