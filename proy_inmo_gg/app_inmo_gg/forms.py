from dataclasses import field
from importlib.metadata import files
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Venta_formulario(forms.Form):
    tipo_prop_v= forms.CharField(max_length=40, required=True)
    localidad_v= forms.CharField(max_length=40, required=True)
    barrio_v= forms.CharField(max_length=40, required=True)
    cant_dormi_v= forms.IntegerField()
    estado_v= forms.BooleanField()
    descrp_v= forms.CharField(required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20}))
    otro_cha_v= forms.CharField(max_length=40, required=True)
    otro_ent_v= forms.IntegerField()

class Alquiler_formulario(forms.Form):
    tipo_prop_a= forms.CharField(max_length=40, required=True)
    localidad_a= forms.CharField(max_length=40, required=True)
    barrio_a= forms.CharField(max_length=40, required=True)
    cant_dormi_a= forms.IntegerField()
    estado_a= forms.BooleanField()
    descrp_a= forms.CharField(required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20}))
    otro_cha_a= forms.CharField(max_length=40, required=True)
    otro_ent_a= forms.IntegerField()

class Turismo_formulario(forms.Form):
    tipo_prop_t= forms.CharField(max_length=40, required=True)
    localidad_t= forms.CharField(max_length=40, required=True)
    barrio_t= forms.CharField(max_length=40, required=True)
    cant_dormi_t= forms.IntegerField()
    estado_t= forms.BooleanField()
    descrp_t= forms.CharField(required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20}))
    otro_cha_t= forms.CharField(max_length=40, required=True)
    otro_ent_t= forms.IntegerField()


#Formulario para editar regustros de usuarios
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ['email', 'password1', 'password2']
        help_text= {k:"" for k in fields}