from django.urls import path, re_path
from .views import index,concier,noti,bandasform, artistas_listado,eliminar,artistas_form,modificar,filtro_busqueda
from . import views
 
urlpatterns = [ 
    path('',index,name='index'),
    path('concier',concier,name='conci'),
    path('noti',noti,name='noti'),
    path('bandasform',bandasform, name='bandasform'),
    path('artistas_listado', artistas_listado, name='artistas_listado'),
    path('eliminar/<id>', eliminar, name='eliminar'),
    path('artistas_form', artistas_form, name='artistas_form'),
    path('modificar/<id>',modificar, name='modificar'),
    path('Filtrar',filtro_busqueda, name='filtro_busqueda'),
] 
