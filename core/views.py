from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Cita, Consultorio

# ==========================================
# VISTAS DE LA UNIDAD 1 (LOGIN)
# ==========================================
def login_view(request):
    return render(request, 'core/login.html')


# ==========================================
# VISTAS DE LA UNIDAD 2 (PACIENTES)
# ==========================================
def lista_pacientes(request):
    query = request.GET.get('q', '')
    if query:
        pacientes = Usuario.objects.filter(username__icontains=query, is_active=True, tipo_usuario='paciente')
    else:
        pacientes = Usuario.objects.filter(is_active=True, tipo_usuario='paciente')
    return render(request, 'core/pacientes.html', {'pacientes': pacientes, 'query': query})

def crear_paciente(request):
    if request.method == 'POST':
        Usuario.objects.create(
            username=request.POST['username'],
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion'],
            sexo=request.POST['sexo'],
            tipo_usuario='paciente'
        )
        return redirect('lista_pacientes')
    return render(request, 'core/form_paciente.html')

def baja_paciente(request, id):
    paciente = get_object_or_404(Usuario, id=id)
    paciente.is_active = False
    paciente.save()
    return redirect('lista_pacientes')


# ==========================================
# VISTAS DE LA UNIDAD 2 (CITAS)
# ==========================================
def agendar_cita(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        medico_id = request.POST.get('medico')
        consultorio_id = request.POST.get('consultorio')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        motivo = request.POST.get('motivo')

        # Entregable 4: Validación de reglas de Citas (Empalme)
        empalme = Cita.objects.filter(medico_id=medico_id, fecha=fecha, hora=hora).exists()
        
        if empalme:
            error = "Error: El médico ya tiene una cita ocupada en ese horario."
            pacientes = Usuario.objects.filter(tipo_usuario='paciente', is_active=True)
            medicos = Usuario.objects.filter(tipo_usuario='medico', is_active=True)
            consultorios = Consultorio.objects.all()
            return render(request, 'core/form_cita.html', {
                'error': error, 'pacientes': pacientes, 
                'medicos': medicos, 'consultorios': consultorios
            })

        # Entregable 3: Agendamiento exitoso
        Cita.objects.create(
            paciente_id=paciente_id,
            medico_id=medico_id,
            consultorio_id=consultorio_id,
            fecha=fecha,
            hora=hora,
            motivo=motivo
        )
        return redirect('lista_pacientes')

    # GET: Cargar datos para el formulario
    pacientes = Usuario.objects.filter(tipo_usuario='paciente', is_active=True)
    medicos = Usuario.objects.filter(tipo_usuario='medico', is_active=True)
    consultorios = Consultorio.objects.all()
    
    return render(request, 'core/form_cita.html', {
        'pacientes': pacientes,
        'medicos': medicos,
        'consultorios': consultorios
    })