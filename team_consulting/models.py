from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=150)
    correo = models.EmailField(max_length=150)
    telefono = models.CharField(max_length=15)  # Mejor usar CharField para números con + o 0
    fecha_cita = models.DateField()
    
    TIPO_OPCIONES = [
        ('seguridad', 'Auditoría de ciberseguridad'),
        ('presupuesto', 'Presupuesto empresarial'),
    ]
    tipo_cita = models.CharField(max_length=20, choices=TIPO_OPCIONES)
    
    comentario = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.nombre_completo} - {self.tipo_cita}"
