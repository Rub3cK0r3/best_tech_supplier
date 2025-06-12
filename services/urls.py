"""
Url config de la app de SERVICIOS
"""
from django.contrib import admin
from django.urls import path
from .views import view as Initial_page
urlpatterns = [
    # '' porque es la principal de mi aplicacion para servicios
    path('',Initial_page,name="ini_serv"),
]
