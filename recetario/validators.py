from django.core.exceptions import ValidationError

##Sus Models deben contener al menos 2 validaciones personalizadas

def nombre_valido(value):
        if any(char.isdigit() for char in value):
            raise ValidationError("El nombre de la receta no puede contener números")

def instrucciones_validas(value):
        palabras = value.split()
        if len(palabras) < 5:
            raise ValidationError('El campo instrucciones debe tener al menos cinco palabras')

def porciones_validas(value):
        if value <= 0:
            raise ValidationError('La cantidad de porciones debe ser mayor a cero')
        
def tiempo_valido(value):
        if value > 1440:
            raise ValidationError('La duración de la receta no puede ser mayor a 24 horas')