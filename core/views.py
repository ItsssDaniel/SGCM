from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

# --- VISTA DE LA UNIDAD 1 (LOGIN) ---
def login_view(request):
    # Aquí va la lógica de tu login de la U1
    return render(request, 'core/login.html')

# --- VISTAS DE LA UNIDAD 2 (PACIENTES) ---
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