from django.shortcuts import render
from . models import Jugete, Usuario

def jugetes(request):
    num_jugete=Jugete.objects.all()
    
    return render(
        request,
        'jugetes.html',
        context={'num_jugete':num_jugete},
    )
# Create your views here.
def sesion(request):
    num_usuario=Usuario.objects.all()
    
    return render(
        request,
        'sesion.html',
        context={'num_usuario':num_usuario},
    )

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

class JugeteDelete(DeleteView):
    model = Jugete
    success_url = reverse_lazy('juegetes')


class JugeteDetailView(generic.DetailView):
    model = Jugete
    
class UsuarioDelete(DeleteView):
    model = Usuario
    success_url = reverse_lazy('sesion')
    
class UsuarioDetailView(generic.DetailView):
    model = Usuario

class UsuarioListView(generic.ListView):
    model = Genre
    template_name = 'templates/peliculas/genre_list.html'
    queryset = Genre.objects.all()

    paginate_by = 10



