from django.db import models
    
# Create your models here.
class Employee(models.Model):
    salary = models.FloatField()
    #Esta sera la primary key de mi tabla
    id = models.AutoField(primary_key=True) #El me lo va a gestionar por detras con un serial
    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=175)
    email = models.EmailField()
    telf = models.CharField(max_length=12)
    puesto = models.TextField()
    esJefe = models.BooleanField()
    esContable = models.BooleanField()
    esComercial = models.BooleanField()
    
    #Por ahora no añadimos Meta para el admin porque aun no lo tenemos