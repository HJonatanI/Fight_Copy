from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Character, Inventario, Mision, MisionActiva
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
	enemigo = Character.objects.exclude(usuario=request.user).order_by('?').first()
	if enemigo:
		# Variables de combate #
		personaje_ataque = personaje.fuerza - (enemigo.defensa * 0.5)
		enemigo_ataque = enemigo.fuerza - (personaje.defensa * 0.5)
		# Determina el daño mínimo #
		personaje_ataque = max(1, personaje_ataque)
		enemigo_ataque = max(1, enemigo_ataque)
		# Registro de eventos de combate #
		log_combate = []
		# Realiza el combate #
		while personaje.salud > 0 and enemigo.salud > 0:
			# Turno del personaje #
			enemigo.salud -= personaje_ataque
			log_combate.append(f"{personaje.nombre} inflige {personaje_ataque} de daño a {enemigo.nombre}. Salud restante del enemigo: {enemigo.salud}")
			if enemigo.salud <= 0:
				resultado = 'victoria'
				break
			# Turno del enemigo #
			personaje.salud -= enemigo_ataque
			log_combate.append(f"{enemigo.nombre} inflige {enemigo_ataque} de daño a {personaje.nombre}. Salud restante del personaje: {personaje.salud}")
			if personaje.salud <= 0:
				resultado = 'derrota'
				break
		# Procesa el resultado #
		if resultado == 'victoria':
			personaje.experiencia += 20
			personaje.oro += 10
			personaje.subir_nivel()
			enemigo.salud = max(1, enemigo.salud)  # Evita que llegue a 0
		else:
			personaje.salud = max(1, personaje.salud)  # Evita que llegue a 0
		personaje.save()
		enemigo.save()
		return render(request, 'game/batalla.html', {
			'personaje': personaje,
			'enemigo': enemigo,
			'resultado': resultado,
			'log_combate': log_combate
		})
	else:
		return HttpResponseRedirect(reverse('perfil_personaje'))
	
@login_required
def misiones_disponibles(request):
	misiones = Mision.objects.all()  # Trae todas las misiones
	misiones_activas = Mision.objects.filter(misionactiva__usuario=request.user)
	misiones_activas_completas = Mision.objects.filter(misionactiva__usuario=request.user, misionactiva__completada=True)
	return render(request, 'game/misiones_disponibles.html', {'misiones': misiones, 'misiones_activas': misiones_activas, 'misiones_activas_completas': misiones_activas_completas})
	
@login_required
def aceptar_mision(request, mision_id):
	mision = get_object_or_404(Mision, id=mision_id)
	MisionActiva.objects.get_or_create(usuario=request.user, mision=mision)
	return redirect('misiones_disponibles')
	
@login_required
def completar_mision(request, mision_id):
	mision = get_object_or_404(Mision, id=mision_id)
    # Obtener la misión activa asociada al usuario y la misión
	mision_activa = get_object_or_404(MisionActiva, mision=mision, usuario=request.user)
	if not mision_activa.completada:
		# Marcar la misión como completada y otorgar recompensas #
		personaje = get_object_or_404(Character, usuario=request.user)
		personaje.experiencia += mision_activa.mision.recompensa_experiencia
		personaje.oro += mision_activa.mision.recompensa_oro
		personaje.save()
		mision_activa.completada = True
		mision_activa.save()
		return redirect('misiones_disponibles')
	else:
		return redirect('misiones_disponibles')

