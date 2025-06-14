from django import forms

class DatosClienteFormulario(forms.Form):
    nombre_completo = forms.CharField(max_length=150, required=True)
    correo = forms.EmailField(max_length=150, required=True)
    telefono = forms.CharField(max_length=20, required=True)
    TIPO_OPCIONES = [
        ('seguridad', 'Auditoría de ciberseguridad'),
        ('presupuesto', 'Presupuesto empresarial'),
    ]
    
    fecha_cita = forms.DateField(required=True)

    tipo_cita = forms.ChoiceField(
        choices=TIPO_OPCIONES,
        required=True,
        label="Tipo de asesoría"
    )
    comentario = forms.CharField(max_length=300, required=True)
    