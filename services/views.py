from django.shortcuts import render,HttpResponse
from employee.models import Employee
from services.models import products
# Create your views here.
def view(request):
    template = 'services/services.html'
    
    asesores = Employee.objects.values('name','surname','telf').filter(puesto='Asesor')
    productos = products.objects.values('name','pvp').order_by('-pvp')[:2]
    ofertas = products.objects.values('name','description')
    context  = {
        'asesores':asesores,
        'productos':productos,
        'ofertas':ofertas
    }
    return render(request,template,context)