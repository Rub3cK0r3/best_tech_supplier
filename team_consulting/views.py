from django.shortcuts import render,HttpResponse
from .forms import DatosClienteFormulario
# Create your views here.
# En este caso no es necesario usar un contexto por lo que no lo renderizo a la template
def first(request):
    template = 'team_consulting/form.html'
    
    if request.method == 'POST':
        form = DatosClienteFormulario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Cliente.objects.create(
                nombre_completo=data['nombre_completo'],
                correo=data['correo'],
                telefono=data['telefono'],
                fecha_cita=data['fecha_cita'],
                tipo_cita=data['tipo_cita'],
                comentario=data['comentario'],
            )
            return redirect('thanks')  # Asegúrate de tener esta ruta en urls.py
        else:
            return render(request, template, {'form': form})
    else:
        form = DatosClienteFormulario()
        return render(request, template, {'form': form})

def gracias(request):
    template_gracias = 'team_consulting/gracias.html'
    return render(request,template_gracias)