from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Tu modelo de Usuario personalizado
class Usuario(AbstractUser):
    TIPOS_USUARIO = (
        ('administrador', 'Administrador'),
        ('medico', 'Médico'),
        ('paciente', 'Paciente'),
        ('recepcionista', 'Recepcionista'),
    )
    
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='paciente')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    sexo = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"

# 2. Tabla Consultorio
class Consultorio(models.Model):
    nombre_consultorio = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_consultorio

# 3. Tabla Citas
class Cita(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas_como_paciente')
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas_como_medico')
    consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL, null=True, blank=True)
    
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f"Cita: {self.fecha} a las {self.hora}"