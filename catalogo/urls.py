

from django.urls import path
from .views.categoria import lista_categoria

urlpatterns = [
    path("categorias/", lista_categoria, name="list_categoria")

]
