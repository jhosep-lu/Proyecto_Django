from rest_framework import serializers
from .models import Receta, RecetaIngrediente, RecetaCatergoria

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"

class RecetaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaIngrediente
        fields = '__all__'

class RecetaCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaCatergoria
        fields = '__all__'