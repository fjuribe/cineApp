from django.urls import path
from .views import home,galeria,listado_pelicula,nueva_pelicula,modificar_pelicula,eliminar_pelicula,registro_usuario

urlpatterns = [
    path('',home,name="home"),
    path('galeria/',galeria,name="galeria"),
    path('listado-pelicula/',listado_pelicula,name="listado_pelicula"),
    path('nueva-pelicula/',nueva_pelicula,name="nueva_pelicula"),
    path('modificar-pelicula/<int:pk>/',modificar_pelicula,name="modificar_pelicula"),
    path('eliminar-pelicula/<int:pk>/',eliminar_pelicula,name="eliminar_pelicula"),
    path('registro/',registro_usuario,name="registro_usuario"),
]
