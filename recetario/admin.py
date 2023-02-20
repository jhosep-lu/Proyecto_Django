from django.contrib import admin

# Register your models here.
from .models import Receta
from .models import Ingrediente
from .models import Categoria
from .models import RecetaIngrediente
from .models import RecetaCatergoria


#admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(Categoria)
#admin.site.register(RecetaIngrediente)
#Sadmin.site.register(RecetaCatergoria)

class RecetaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "instrucciones", "porciones", "tiempo_preparacion",)
    ordering = ["tiempo_preparacion"]
    search_fields = ["nombre"]

admin.site.register(Receta, RecetaAdmin)

class RecetaIngredientesAdmin(admin.ModelAdmin):
    list_display = ("receta", "ingrediente", "cantidad",)
    ordering = ["cantidad"]
    search_fields = ["receta"]

admin.site.register(RecetaIngrediente, RecetaIngredientesAdmin)

class RecetaCategoriaAdmin(admin.ModelAdmin):
    list_display = ("receta", "Categoria",)
    search_fields =["receta"]

admin.site.register(RecetaCatergoria,RecetaCategoriaAdmin)
