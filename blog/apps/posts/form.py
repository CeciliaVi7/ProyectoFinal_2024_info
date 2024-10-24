from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import User,Posts

class RegistroForm(UserCreationForm):
    username=forms.CharField(max_length=250)
    email=forms.EmailField(max_length=250, help_text='Required')
    password1=forms.CharField (widget=forms.PasswordInput, required=True)
    password2=forms.CharField (widget=forms.PasswordInput, required=True)
    icono= forms.ImageField(label="imagen de perfil", required=False)
    class Meta:
        model= User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
            'icono',

        ]

class CrearForm(forms.ModelForm):

    class Meta:
        model = Posts
        exclude = ["autor"]