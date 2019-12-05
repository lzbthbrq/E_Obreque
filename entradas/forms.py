from django import forms
from django.forms import ModelForm
from .models import Artistas,Genero
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArtistasForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)
    discos = forms.IntegerField(min_value=1,max_value=100)
    n_integrantes = forms.IntegerField(min_value=1)

    
    class Meta:
        model=Artistas
        fields =['nombre','nacionalidad','discos','fundacion','n_integrantes','gen']
        
        widgets = {
            'fundacion': forms.SelectDateWidget(years=range(1980,2020))
        }

    def clean_fundacion(self):
        funda = self.cleaned_data['fundacion']

        if funda > datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser superior al dia de hoy")
        return funda



class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password1','password2']