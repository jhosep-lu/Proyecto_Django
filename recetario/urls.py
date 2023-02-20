from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views


router = DefaultRouter()
router.register(r"recetas", views.RecetaViewSet)
router.register(r'receta-ingredientes', views.RecetaIngredienteViewSet)
router.register(r'receta-categorias', views.RecetaCategoriaViewSet)

urlpatterns = [
    path("contact/<str:name>", views.contact, name="contact" ),
    path("categorias", views.categorias, name="categorias"),
    path("recetas", views.recetaFormView, name="recetas"),
    path("recetas/contador/", views.receta_count,name="contador"),
    #path("", views.index, name="index")
    path("", include(router.urls))
]


