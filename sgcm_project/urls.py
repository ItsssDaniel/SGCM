from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    
    # --- Fíjate muy bien en el "name" de estas tres ---
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/eliminar/<int:id>/', views.baja_paciente, name='baja_paciente'),
    
    path('citas/agendar/', views.agendar_cita, name='agendar_cita'),
]