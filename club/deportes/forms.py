from django import forms

class RegistroJugadores (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField ()
    edad = forms.IntegerField()
    estatura = forms.IntegerField()
    deporte = forms.CharField()
    
class RegistroFutbol (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField ()
    posicion = forms.IntegerField()
    
class RegistroBasquet (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField ()
    posicion = forms.IntegerField()
  
    
class RegistroRugby (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField ()
    posicion = forms.CharField()
      