from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Artistas,Genero,Tickets,Conciertos,Suscriptor
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import ArtistasForm,CustomUserForm
from django.contrib.auth import login,authenticate

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

@permission_required('entradas.add_artistas')
def artistas_form(request):
    data = {
        'form':ArtistasForm()
    }

    if request.method == 'POST':  #se valida si hay datos
        formulario = ArtistasForm(request.POST) # se crea el formulario
        if formulario.is_valid():  # Se valida si el formulario es de tipo post
            formulario.save() # Se guarda en la bd
            data['mensaje'] = "GUARDADO CORRECTAMENTE!" 
        data['forms'] = formulario
    return render(
        request, 'artistas_form.html',data # se devuelve a la pagina
    )

def artistas_listado(request):
    arti = Artistas.objects.all()
    data ={
        'arti':arti
    }

    return render(
        request,
        'filtro_busqueda.html', data
        )

def eliminar(request,id):
    arti=Artistas.objects.get(id=id)
    arti.delete()

    return redirect(to='filtro_busqueda')
  
def modificar(request,id):
    arti = Artistas.objects.get(id=id) #recibe por aprametro la columna que vamos a buscar
    data ={
        'form': ArtistasForm(instance=arti)
    }
    if request.method =='POST':
        formulario = ArtistasForm(data=request.POST, instance=arti)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "MODIFICADO CORRECTAMENTE"
            data['form'] = formulario #se sobre escribe a variable guardando los nuevos datos
        data['forms'] = formulario
        
    return render(request, 'modificar.html', data)


def filtro_busqueda(request):
    artis= Artistas.objects.all()

    if request.POST.get('nomb'):
        nomb = request.POST.get('nomb')
        artis = artis.filter(nombre__contains=nomb)
    elif request.POST.get('gen'):
        gen = request.POST.get('gen')
        artis = artis.filter(gen__nomg__icontains=gen)

    return render(request, 'filtro_busqueda.html', {'artis': artis} )

def registrar(request):
    data ={
       'form':CustomUserForm() 
    }
    if request.method == "POST":
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='index')
    
    return render(request, 'registration/registrar.html', data)
