from django.db import models
from django.urls import reverse #se utiliza para la clase instancia de libros... son modulos que necesita django
import uuid 
# Create your models here.

class Suscriptor(models.Model):
    nickname = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    f_nacimiento = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.nickname}, {self.correo}'

class Genero(models.Model):
    nomg = models.CharField(max_length=200)
    def __str__(self):
        return self.nomg

class Artistas(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    nacionalidad = models.CharField(max_length=200, default="")
    discos = models.IntegerField()
    fundacion = models.DateField(null=True)
    n_integrantes = models.IntegerField()
    gen = models.ForeignKey('Genero',on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        ordering = ['nombre','nacionalidad']

    def __str__(self):
        return f'{self.nombre}, ({self.nacionalidad})'


class Tickets(models.Model):
    cantidad = models.IntegerField(default=0)
    artista = models.ForeignKey('Artistas',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.cantidad)

class Conciertos(models.Model):
    artista = models.ForeignKey('Artistas',on_delete=models.SET_NULL,null=True)
    fecha_concierto = models.DateField(null=True,blank=True)
    lugar =  models.CharField(max_length=200)
    
    def __str__(self):
        """String for represeting the Model object"""
        return f'{self.fecha_concierto} ({self.artista.nombre})'
