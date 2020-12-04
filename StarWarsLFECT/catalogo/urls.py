from django.urls import path 
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('Jugete/', views.Jugete, name='jugetes'),
    path('Usuario/', views.UsuarioListView.as_view(), name='sesion'),
    path('Jugete/<int:pk>', views.JugeteDetailView.as_view(), name='Jugete-detail'),
    path('Usuario/<str:pk>', views.UsuarioDetailView.as_view(), name='Usuario-detail'),
    
    
]

urlpatterns += [
    path('Jugete/create/', views.genre_new,name='juegete_create'),
    path('Jugete/<int:pk>/update/', views.Jugete_edit, name='Jugete_update'),
    path('Jugete/<int:pk>/delete/', views.JugeteDelete.as_view(), name='Jugete_delete'),
    path('Usuario/create/', views.Usuario_new,name='Usuario_create'),
    path('Usuario/<str:pk>/update/', views.Usuario_edit, name='Usuario_update'),
    path('Usuario/<str:pk>/delete/', views.UsuarioDelete.as_view(), name='Usuario_delete'),
]


