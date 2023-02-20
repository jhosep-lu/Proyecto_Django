from django.db import models
from .validators import nombre_valido, instrucciones_validas, porciones_validas, tiempo_valido
# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=150, unique=True, error_messages={'unique': 'Ya existe una receta con ese nombre.'}, validators=[nombre_valido])
    instrucciones = models.TextField(validators=[instrucciones_validas])
    porciones  = models.IntegerField(validators=[porciones_validas])
    tiempo_preparacion = models.PositiveSmallIntegerField(validators=[tiempo_valido])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete= models.CASCADE)
    cantidad = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class RecetaCatergoria(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
