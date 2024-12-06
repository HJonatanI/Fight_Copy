from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Character, Inventario
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

# Create your views here.

@login_required
def perfil_personaje(request):
	# Obtener el personaje del usuario #
	personaje = get_object_or_404(Character, usuario=request.user)
	return render(request, 'game/perfil.html', {'personaje': personaje})

@login_required
def inventario(request):
	personaje = get_object_or_404(Character, usuario=request.user)
	inventario = Inventario.objects.filter(personaje=personaje)
	return render(request, 'game/inventario.html', {'inventario': inventario, 'personaje': personaje})

    	
@login_required
def batalla(request):
	personaje = get_object_or_404(Character, usuario=request.user)
	enemigo = Character.objects.exclude(usuario=request.user).order_by('?').first()  # Selecciona un enemigo al azar
	if enemigo:
		# Simulación simple de combate #
		resultado = random.choice(['victoria', 'derrota'])
		if resultado == 'victoria':
			personaje.experiencia += 10
			personaje.oro += 5
			personaje.save()
			return render(request, 'game/batalla.html', {'personaje': personaje, 'enemigo': enemigo, 'resultado': resultado})
		else:
			return render(request, 'game/batalla.html', {'personaje': personaje, 'enemigo': enemigo, 'resultado': resultado})
	else:
		return HttpResponseRedirect(reverse('perfil_personaje'))
