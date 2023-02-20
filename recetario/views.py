from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Receta, RecetaIngrediente, RecetaCatergoria
from .forms import RecetaForm
from rest_framework import viewsets
from .serializers import RecetaSerializer, RecetaIngredienteSerializer, RecetaCategoriaSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

def categorias(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre = post_nombre)
        q.save()
    filtro_nombre = request.GET.get('filtro_nombre')
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
        
    return render(request, "form_categorias.html",{
        "categorias": categorias
    })

def recetaFormView(request):
    form = RecetaForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_receta.html",{
        "form": form
    })
##Utilice Django Rest Framework para crear al menos 3 ModelViewSet o GenericAPIView
class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class RecetaIngredienteViewSet(viewsets.ModelViewSet):
    queryset = RecetaIngrediente.objects.all()
    serializer_class = RecetaIngredienteSerializer

class RecetaCategoriaViewSet(viewsets.ModelViewSet):
    queryset = RecetaCatergoria.objects.all()
    serializer_class = RecetaCategoriaSerializer

## Utilice Django Rest Framework para crear al menos 1 Custom API

@api_view(["GET"])
def receta_count(request):
    try:
        cantidad = Receta.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)