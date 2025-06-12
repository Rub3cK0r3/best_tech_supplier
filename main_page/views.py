from django.shortcuts import render,HttpResponse
from services.models import products
# Create your views here.
def view(request):
    
    template = 'main_page/presentation.html'
    producto = products.objects.values('name','pvp')
    
    context = {
        'productos': producto
    }
    
    return render(request,template,context)