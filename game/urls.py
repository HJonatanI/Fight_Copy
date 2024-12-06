from django.urls import path
from . import views
	
urlpatterns = [
	path('perfil/', views.perfil_personaje, name='perfil_personaje'),
	path('inventario/', views.inventario, name='inventario'),
	path('batalla/', views.batalla, name='batalla'),
]