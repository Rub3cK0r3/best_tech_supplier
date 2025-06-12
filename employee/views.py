from django.shortcuts import render,HttpResponse
from .models import Employee
# Create your views here.
def view(request):
    template = 'employee/employee.html'
    
    empleados = Employee.objects.values('name','surname','puesto')
    context = {
        'empleados':empleados
    }
    return render(request,template,context)