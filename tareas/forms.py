from django import forms
from .models import registroTareas, Prioridad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class registroForm(forms.ModelForm):
    
    class Meta:
        fecha_vencimiento_tarea = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))
        model = registroTareas
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asignado_a'].queryset = User.objects.all()  # Permite seleccionar cualquier usuario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prioridad'].queryset = Prioridad.objects.all()  # Permite seleccionar cualquier prioridad


class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True, 
        label="Nombre de usuario", 
        error_messages={'required': 'Su nombre es requerido'})
    password = forms.CharField(widget=forms.PasswordInput, 
        max_length=20, required=True, 
        label="Contraseña", 
        error_messages={'required': 'Contraseña es obligatoria'})


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']