from django.contrib import admin
from django.urls import path
from .views import view as main
urlpatterns = [
    path('',main,name="main"),
]