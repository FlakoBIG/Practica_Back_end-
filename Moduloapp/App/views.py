from django.shortcuts import render
from App.forms import FormPersonaje
from App.models import Personaje

# Create your views here.
def index(request):
    return render(request,'index.html')

def listadopersonajes(request):
    personajes = Personaje.objects.all()
    data = {'personajes': personajes}
    return render(request, 'ListaPersonajes.html', data)


def agregarPersonaje(request):
    form = FormPersonaje()
    if request.method == 'POST':
        form = FormPersonaje(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'AgregarPersonaje.html',data)

def  eliminarPersonaje(request,id):
    personajes=Personaje.objects.get(id=id)
    personajes.delete()
    return render(request,'ListaPersonajes.html')

def actualizarPersonaje(request,id):
    personajes=Personaje.objects.get(id=id)
    form=FormPersonaje(instance=personajes)
    if request.method=='POST':
        form=FormPersonaje(request.POST,instance=personajes)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'AgregarPersonaje.html',data)