from django.db import models

class jugadores (models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField (max_length=50)
    edad = models.IntegerField()
    estatura = models.IntegerField()
    deporte = models.CharField(max_length=50)

class Futbol (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField (max_length=50)
    posicion = models.IntegerField()

class Basquet (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField (max_length=50)
    posicion = models.IntegerField()
    
class Rugby (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField (max_length=50)
    posicion = models.CharField(max_length=50)

# Create your models here.
