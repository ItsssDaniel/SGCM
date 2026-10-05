from django.test import TestCase
from .models import Usuario, Consultorio, Cita

class CitaTestCase(TestCase):
    def setUp(self):
        # 1. Preparamos los datos de prueba (Médico, Paciente, Consultorio)
        self.medico = Usuario.objects.create(username="Dr. House", tipo_usuario="medico", is_active=True)
        self.paciente = Usuario.objects.create(username="Carlos Paciente", tipo_usuario="paciente", is_active=True)
        self.consultorio = Consultorio.objects.create(nombre_consultorio="Consultorio Principal")
        
        # 2. Creamos una cita inicial ocupando el horario de las 10:00 AM
        Cita.objects.create(
            paciente=self.paciente,
            medico=self.medico,
            consultorio=self.consultorio,
            fecha="2026-10-15",
            hora="10:00:00",
            motivo="Chequeo general"
        )

    def test_validacion_empalme_cita(self):
        """Prueba que el sistema rechace una cita en un horario ya ocupado por el médico"""
        
        # 3. Hacemos una petición POST simulando que alguien llena el formulario con el MISMO horario
        response = self.client.post('/citas/agendar/', {
            'paciente': self.paciente.id,
            'medico': self.medico.id,
            'consultorio': self.consultorio.id,
            'fecha': '2026-10-15',
            'hora': '10:00:00',
            'motivo': 'Dolor de cabeza'
        })
        
        # 4. Verificamos que la página cargue mostrando el mensaje de error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Error: El médico ya tiene una cita ocupada en ese horario.")
        
        # 5. Verificamos que la base de datos siga teniendo solo 1 cita (no se guardó la duplicada)
        self.assertEqual(Cita.objects.count(), 1)