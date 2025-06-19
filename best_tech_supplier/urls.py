"""
URL configuration for best_tech_supplier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# From MDN Django Tutorials
# # Use include() to add paths from other applications
from django.urls import path,include

from services import urls as urls_services
from employee import urls as urls_employees
from main_page import urls as Main_page
from team_consulting import urls as Form_page
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(Main_page), name="Main"),
    
    #Para la mejor modularizacion importo todos las views de las vistas de cada una de las aplicaciones
    #en las cuales los hare por separado (principio de responsabilidad unica)
    path('services/',include(urls_services), name="servicios"),
    path('our-team/',include(urls_employees), name="empleados"),
    path('booking/',include(Form_page),name="booking_form")
]
