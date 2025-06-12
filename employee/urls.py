"""
Url config de la app de EMPLEADOS
"""
from django.contrib import admin
from django.urls import path,include
from .views import view as Initial_page
from services import views as Services_Page
urlpatterns = [
    # '' porque es la principal de mi vista de empleados
    path('',Initial_page,name="ini_emp"),
]
