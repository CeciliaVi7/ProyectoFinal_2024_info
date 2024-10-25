from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Posts,Comentarios

class RegistroForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Nombre de usuario",
            "style": "width: 300px;"  # Ajusta el ancho 
        })
    )
    email = forms.EmailField(
        max_length=250,
        help_text='Obligatorio. Longitud máxima de 150 caracteres.',
        widget=forms.EmailInput(attrs={
            "class": "form-control", 
            "placeholder": "name@example.com",
            "style": "width: 300px;"  # Ajusta el ancho
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control", 
            "placeholder": "Contraseña",
            "style": "width: 300px; border-radius: 5px;"  #estilo redondeado
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control", 
            "placeholder": "Confirmar contraseña",
            "style": "width: 300px; border-radius: 5px;"  #estilo redondeado
        })
    )
    icono = forms.ImageField(
        label="Imagen de perfil", 
        required=False, 
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "style": "width: 300px;"  # Ajusta el ancho
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'icono']


class CustomLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="Recuérdame")    


class CrearForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ["autor"]


class ModificarForm(forms.ModelForm):  
    class Meta:
        model = Posts
        fields = ("contenido",)

#Formulario de Comentarios
class ComentarioForm(forms.ModelForm):
    model= Comentarios
    fields=["contenido",]

class ModificarComentarioForm(forms.ModelForm):

    class Meta:
        model= Comentarios
        fields = ['contenido']

