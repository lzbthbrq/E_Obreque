from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Artistas,Genero,Tickets,Conciertos,Suscriptor
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html',)

def concier(request):
    return render(request,'conci.html',)

def noti(request):
    return render(request, 'noti.html',)

def bandasform(request):
    return render(
        request,
        'bandasform.html',
        )

def artistas_form(request):
    arti = Artistas.objects.all()
    genero= Genero.objects.all()
    var = {
        'arti': arti,
        'genero':genero
    }

    if request.POST:
        arti = Artistas()
        arti.nombre = request.POST.get('txtnombre')
        arti.nacionalidad = request.POST.get('txtnacionalidad')
        arti.discos = request.POST.get('txtcds')
        arti.fundacion = request.POST.get('dtinicio')
        arti.n_integrantes = request.POST.get('txtintegra')
        gene = Genero()
        gene.id = request.POST.get('cbogen')
        arti.gen = gene

        try:
            arti.save()
            var['mensaje'] = 'Guardado Correctamente'
        except:
            var['mensaje'] = 'No se ha podido guardar'

    return render(
        request, 'artistas_form.html',var
    )

def artistas_listado(request):
    arti = Artistas.objects.all()

    return render(
        request,
        'artistas_listado.html', {'arti':arti}
        )

def eliminar(request,id):
    arti=Artistas.objects.get(id=id)

    try:
        arti.delete()
        mensaje="Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar Correctamente"
        messages.success(request, mensaje)

    return redirect('filtro_busqueda')
  
def modificar(request,id):
    arti = Artistas.objects.get(id=id)
    genero = Genero.objects.all()
    var ={
        'arti':arti,
        'genero': genero
    }

    if request.POST:
        arti = Artistas()
        arti.id = request.POST.get('txtid')
        arti.nombre = request.POST.get('txtnombre')
        arti.nacionalidad = request.POST.get('txtnacionalidad')
        arti.discos = request.POST.get('txtcds')
        arti.fundacion = request.POST.get('dtinicio')
        arti.n_integrantes = request.POST.get('txtintegra')
        gene = Genero()
        gene.id = request.POST.get('cbogen')
        arti.gene = gene

        try:
            arti.save()
            messages.success(request, 'Modificado Correctamente')
        except:
            messages.error(request, 'No se ha modificado')

    return render(request, 'modificar.html', var)


def filtro_busqueda(request):
    artis= Artistas.objects.all()

    if request.POST.get('nomb'):
        nomb = request.POST.get('nomb')
        artis = artis.filter(nombre__contains=nomb)
    elif request.POST.get('gen'):
        gen = request.POST.get('gen')
        artis = artis.filter(gen__nomg__icontains=gen)

    return render(request, 'filtro_busqueda.html', {'artis': artis} )
