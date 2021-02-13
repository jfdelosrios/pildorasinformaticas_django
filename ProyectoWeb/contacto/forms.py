from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", requires=True)
    email=forms.CharField(label="Email", requires=True)
    contenido=forms.CharField(label="Contenido")