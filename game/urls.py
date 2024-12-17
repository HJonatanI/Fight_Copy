from django.urls import path
from . import views
	
urlpatterns = [
	path('perfil/', views.perfil_personaje, name='perfil_personaje'),
	path('inventario/', views.inventario, name='inventario'),
	path('batalla/', views.batalla, name='batalla'),
	path('misiones/', views.misiones_disponibles, name='misiones_disponibles'),
	path('misiones/aceptar/<int:mision_id>/', views.aceptar_mision, name='aceptar_mision'),
	path('misiones/completar/<int:mision_id>/', views.completar_mision, name='completar_mision'),
]