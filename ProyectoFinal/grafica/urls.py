from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), # Definir la ruta principal de la app
]