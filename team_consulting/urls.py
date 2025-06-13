"""
Url config de la app de ASESORES
"""
from django.contrib import admin
from django.urls import path,include
from .views import first as Consulting_form_page
from .views import gracias as thanks_page
urlpatterns = [
    # '' porque es la principal de mi vista de empleados
    path('',Consulting_form_page,name="ini_form"),
    path('gracias/',thanks_page,name="thanks"),
]