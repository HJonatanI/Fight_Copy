# Fight_Copy #

Repositorio de prueba para proyecto de diseño web.

---------------------------------------------------------------------
---------------------------------------------------------------------

## Parte 1: Configuración del entorno de desarrollo. ##

### Paso 1: Crear una cuenta en GitHub. ###

* Entrar a https://github.com/, registrarse y completar el proceso de verificación.
	* En la página de inicio, entrar en la opción Sing up.
	* Ingresar email.
	* Ingresar contraseña.
	* Ingresar nombre de usuario.
	* Aceptar o no propagandas al email.
	* Confirmación de “No eres un robot”.
	* Presionar en “Create Account”.
	* Si todo es correcto se enviará un mail de confirmación al email ingresado.

### Paso 2: Crear un repositorio en GitHub. ###

1. Una vez dentro de la cuenta de GitHub, presionar en New para crear un nuevo repositorio.

2. Completar los siguientes campos:
	* Repository name: nombre del repositorio, por ejemplo Fight_Copy.
	* Description: una breve descripción del repositorio.
	* Public: para que otros puedan verlo (o Private si se prefiere).
	* Marcar la casilla Add a README file para incluir un archivo README.md en el repositorio.
	* Existen dos opciones más que se dejarán en blanco: Add .gitignore y Choose a license.

3. Hacer clic en Create repository.

### Paso 3: Configurar Git en el ordenador. ###

1. Instalar Git:
	* En Windows, descargar Git desde https://git-scm.com/ e instalar de forma automática dando a todo Siguiente.
	* En macOS, se puede instalar Git a través de Homebrew:
	brew install git
        
2. Abrir una terminal (Git Bash en Windows o la terminal en macOS/Linux) y configurar Git:
	```
	git config --global user.name "TuNombreDeUsuario"
	git config --global user.email "TuCorreo@ejemplo.com"
	```
	Colocar el nombre de usuario y el email de GitHub.

3. Clonar el repositorio:
	* Navegar a la ubicación donde se desea clonar el repositorio:
		```
		cd ruta/donde/guardar/el/proyecto
		```
	* Clonar el repositorio con el enlace de GitHub:
    	```
    	git clone https://github.com/TuUsuario/Fight_Copy.git
		```
	El enlace se encuentra en el repositorio, en la opción <>Code en las pestañas Local/HTTPS.
	* Esto creará una carpeta Fight_Copy con el repositorio descargado.
	
### Paso 4: Instalar Python y MySQL. ###

* Python:
	* Descargar desde https://www.python.org/downloads/ y seguir los pasos de instalación (No olvidarse de marcar la opción de PATH).
	* Verificar la instalación:
		```
		python --version
		```

* MySQL:
	* Descargar MySQL desde https://dev.mysql.com/downloads/mysql/ y seguir los pasos (elegir la instalación completa).
	* Si se está en Windows es necesario configurar el PATH como se indica para Sublime Text.
	* Crear una base de datos básica.
		* Abrir MySQL: Abrir una terminal y ejecutar `mysql -u root -p` o `winpty mysql -u root -p` (se puede reemplazar root por el usuario configurado en la instalación). Esto abrirá la consola de MySQL y pedirá la contraseña.
		* Crear la Base de Datos: Una vez dentro de MySQL, ejecutar el comando para crear una base de datos. En este caso, la base de datos se llamará fight_copy.
    		```
    		CREATE DATABASE fight_copy;
    		```
		* Crear un Usuario y Asignar Permisos (opcional): Crear un nuevo usuario específicamente para esta base de datos.
			```
			CREATE USER 'tu_usuario'@'localhost' IDENTIFIED BY 'tu_contraseña';
			```
		* Luego, otorgar permisos completos a este usuario en la base de datos:
			```
			GRANT ALL PRIVILEGES ON fight_copy.* TO 'tu_usuario'@'localhost';
    		FLUSH PRIVILEGES;
    		```
		* Verificar la creación de la Base de Datos: Ejecutar el siguiente comando para asegurar de que la base de datos fue creada correctamente:
			```
			SHOW DATABASES;
			```
		Debería verse fight_copy en la lista de bases de datos.

### Paso 5: Configurar un entorno virtual. ###

1. Navegar al directorio del repositorio:
	```
	cd Fight_Copy
	```

2. Crear un entorno virtual:
	```
	python -m venv env
	```

3. Activar el entorno virtual:
	* En Windows:
		```
		.\env\Scripts\activate
		```
	* En macOS/Linux:
		```
		source env/bin/activate
		```
	* En Windows, Git Bash:
		```
		source env/Scripts/activate
		```

4. Para desactivar el entorno virtual:
	```
	deactivate
	```

### Paso 6: Instalar Django. ###

1. Con el entorno virtual activado, instalar Django:
	```
	pip install django
	```

2. Verificar la instalación:
	```
	django-admin --version
	```

3. Mantener un registro con las librerías instaladas en el entorno virtual.
	* Tener activado el entorno virtual (obligatorio).
	* Usar el siguiente comando para crear un archivo requirements.txt:
	```
	pip freeze > requirements.txt
	```
	* El archivo se creará en la dirección actual y tendrá un contenido parecido al siguiente:
	```
	asgiref==3.8.1
	Django==5.1.3
	mysqlclient==2.2.6
	sqlparse==0.5.2
	tzdata==2024.2

	```

4. Instalar las dependencias:
	```
	pip install -r requirements.txt  # Instalar las dependencias
	```

### Paso 7: Instalar Sublime Text y configurarlo. ###

1. Descargar e instalar Sublime Text desde https://www.sublimetext.com/.
	* Si se está en Windows se necesitará configurar el PATH.
	* Buscar en la lupa de inicio “Variables de entorno” del sistema.
	* En la sección de “Variables de sistema” buscar el PATH y presionar en Editar.
	* Seleccionar Nuevo o Add e ingresar la ruta de Sublime Text hasta el directorio donde está el ejecutable.
	* Presionar en Aceptar.

2. Abrir el repositorio con Sublime Text:
	* En la terminal:
		```
		subl .
		```
	* Alternativamente se puede abrir Sublime y usar File > Open Folder para seleccionar la carpeta del repositorio.
	
### Paso 8: Guardar todo en el repositorio local y en el repositorio remoto. ###

1. Guardar todos los cambios en el repositorio local:
	```
	git add .
	git commit -m "Parte ?: Lo que se hace en esa parte"
	```

2. Guardar todos los cambios en el repositorio remoto:
	```
	git push origin main
	```

---------------------------------------------------------------------
---------------------------------------------------------------------

## Parte 2: Crear la estructura básica del proyecto en Django. ##

### Paso 1: Crear un proyecto de Django en el entorno local. ###

1. Activar el entorno virtual:
	```
	.\env\Scripts\activate  # En Windows
	# o
	source env/bin/activate  # En macOS/Linux
	# o
	source env/Scripts/activate  # En Windows con GitBash
	```

2. En la terminal, navegar al directorio del repositorio y usar el siguiente comando para crear el proyecto de Django:
	```
	django-admin startproject fight_copy .
	```
	El punto (.) al final indica a Django que cree los archivos del proyecto en el directorio actual, en lugar de crear una carpeta adicional.

3. Después de ejecutar el comando, se generarán algunos archivos y carpetas en el proyecto:
	* fight_copy/ (directorio del proyecto)
	* __init__.py: avisa a Django que trate este directorio como un módulo de Python.
	* settings.py: contiene toda la configuración del proyecto (base de datos, aplicaciones, middleware, etc.).
	* urls.py: administra todas las rutas o URLs del proyecto.
	* wsgi.py y asgi.py: archivos que permiten que el proyecto se comunique con el servidor web.
	* manage.py: una herramienta para ejecutar comandos de Django (cómo iniciar el servidor, aplicar migraciones, y más).

4. Para verificar que el proyecto se haya creado correctamente, iniciar el servidor de desarrollo de Django:
	```
	python manage.py runserver
	```
	Abrir el navegador y visitar http://127.0.0.1:8000/. Se debería ver una pantalla de bienvenida de Django indicando que el proyecto está funcionando.

### Paso 2: Conocer los archivos de configuración y estructura básica de Django. ###

Antes de continuar, es importante entender la función de los archivos principales en la estructura del proyecto:

* settings.py: este archivo contiene todas las configuraciones del proyecto, como la configuración de la base de datos, aplicaciones instaladas, configuraciones de seguridad y más. Se cambiarán varias configuraciones aquí a medida que avance el proyecto.

* urls.py: en este archivo se definen las URLs principales del proyecto. Al añadir más aplicaciones, se podrán organizar las URLs de manera modular.

* manage.py: este archivo es una interfaz de línea de comandos para interactuar con el proyecto. Se usará para ejecutar el servidor, aplicar cambios en la base de datos, y realizar otras tareas administrativas.

### Paso 3: Configurar Django para conectar con MySQL. ###

1. Abrir settings.py en el directorio fight_copy.

2. Buscar la sección DATABASES. Cambiar la configuración predeterminada para conectar a MySQL. Reemplazar el contenido de DATABASES con el siguiente código:
	```
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'nombre_base_datos', # Cambiar este valor con el nombre de la base de datos
			'USER': 'tu_usuario', # Cambiar este valor con el usuario de MySQL
			'PASSWORD': 'tu_contraseña', # Cambiar este valor con la contraseña del usuario
			'HOST': 'localhost', # Dejar 'localhost' si la base de datos está en el ordenador
			'PORT': '3306', # Puerto predeterminado de MySQL
		}
	}
	```

3. Instalar el conector de MySQL para Python, llamado mysqlclient, con el siguiente comando:
	```
	pip install mysqlclient
	```

4. Para comprobar que la conexión a la base de datos esté configurada correctamente, ejecutar:
	```
	python manage.py migrate
	```
	Esto aplicará las migraciones predeterminadas y debería crear las tablas básicas en la base de datos MySQL que se especificó.

### Paso 4: Crear una aplicación en Django para la lógica del juego. ###

Django utiliza aplicaciones para organizar funcionalidades. Se creará una aplicación para gestionar la lógica y el contenido principal del juego, como los usuarios, los personajes, el sistema de combate, etc.

1. En la terminal, asegurarse de estar en el directorio del proyecto y ejecutar el siguiente comando para crear una aplicación llamada game:
	```
	python manage.py startapp game
	```

2. Después de ejecutar el comando, se verá una nueva carpeta llamada game con los siguientes archivos y directorios:
	* migrations/: almacena las migraciones de la base de datos para esta aplicación.
	* admin.py: registra modelos para gestionarlos en la interfaz de administración de Django.
	* apps.py: permite a Django reconocer esta aplicación como parte del proyecto.
	* models.py: define las tablas de la base de datos en forma de modelos.
	* views.py: se escriben las funciones que manejan las solicitudes de los usuarios (vistas).
	* tests.py: se usa para realizar pruebas automáticas a la aplicación.
	* urls.py: este archivo no está creado por defecto, se añadirá más adelante para definir rutas específicas de la aplicación game.

3. Ahora se debe informar a Django que la aplicación game forma parte del proyecto. Abrir settings.py y buscar la sección INSTALLED_APPS. Añadir game al final de la lista:
	```
	INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'game',  # La aplicación del juego
	]
	```
	Django permite dividir la funcionalidad del proyecto en aplicaciones, y cada aplicación puede tener su propio conjunto de vistas, modelos y rutas. Para entender el flujo:

4. Modelos (models.py): Aquí se definen los modelos que representan las tablas en la base de datos. Por ejemplo, para los personajes de los jugadores, se crea un modelo Character.

5. Vistas (views.py): Las vistas procesan las solicitudes y devuelven respuestas. Cada vista puede representar una página del juego, como el perfil del personaje o la interfaz de combate.

6. URLs (urls.py): Cada aplicación puede tener su propio archivo de URLs para organizar sus rutas de manera modular y luego vincularse con el urls.py principal del proyecto.

---------------------------------------------------------------------
---------------------------------------------------------------------

## Parte 3: Crear los Modelos para la Base de Datos en Django. ##

### Objetivo: ###

Definir las tablas principales para el juego usando modelos de Django y reflejar estos modelos en la base de datos MySQL.

### Paso 1: Planificación de los modelos. ###

Para organizar la estructura de datos del juego, se identificarán los elementos. Antes de utilizar los modelos que se crean en esta parte, se debe eliminar de la base de datos ciertos datos de la migración “admin” anterior ya que si no se hace se generará un error en el orden de la migración “game”.
```
mysql -u root -p
USE fight_copy;
DELETE FROM django_migrations WHERE app='admin';
DROP TABLE IF EXISTS django_admin_log;
```

A continuación, se muestran algunos modelos básicos. Se puede ampliar la lista a medida que el juego crezca.

1. Usuario: Información sobre cada usuario registrado en el juego.

2. Personaje (Character): Detalles de cada personaje, como nivel, experiencia, vida, etc.

3. Inventario: Una lista de objetos o equipo que cada personaje posee.

4. Batalla (Battle): Registros de las batallas entre personajes.

5. Objeto (Item): Definición de los objetos disponibles en el juego.

### Paso 2: Crear el modelo de Usuario en models.py. ###

Django ya incluye un sistema de autenticación de usuarios, se puede aprovechar esto y extender el modelo de usuario predeterminado de Django para agregar atributos específicos. Se dejará todo preparado para dicha modificación si es necesaria.

1. Abrir models.py dentro de la carpeta game.

2. Añadir el siguiente código para crear el modelo de Usuario personalizado:
	```
	from django.contrib.auth.models import AbstractUser
	from django.db import models
    	
	class Usuario(AbstractUser):
		# Se pueden agregar más atributos aquí según lo que se necesite para el juego #
		pass
	```

3. Para que Django use este modelo de usuario personalizado, se abre settings.py y se añade esta línea:
	```
	AUTH_USER_MODEL = 'game.Usuario'
	```
	Esto le indica a Django que utilice el modelo Usuario que se creó en lugar del modelo de usuario predeterminado. También cabe aclarar que todos los modelos en DJango heredan los campos de su superclase, en este caso de AbstractUser que ya tiene campos adicionales.

### Paso 3: Crear el modelo de Personaje (Character). ###

Cada usuario puede tener un personaje asociado en el juego con sus propias estadísticas. Definir este modelo.

* En models.py, añadir el modelo de Character:
	```
	class Character(models.Model):
		usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, related_name='character')
		nombre = models.CharField(max_length=50)
		salud = models.IntegerField(default=100)
		fuerza = models.IntegerField(default=10)
		defensa = models.IntegerField(default=5)
		nivel = models.IntegerField(default=1)
		experiencia = models.IntegerField(default=0)
		oro = models.IntegerField(default=100)
	
		def __str__(self):
			return f"{self.nombre} (Nivel {self.nivel})"
	```

* usuario: Cada personaje pertenece a un usuario específico, y se usa una relación OneToOne para garantizar que cada usuario tenga un único personaje. El primer parámetro se puede declarar sin comillas pero al hacerlo se tiene que asegurar que el modelo mencionado exista con anterioridad, con las comillas se evita el predicamento haciendo que las modificaciones sean más dinámicas. Con ` related_name='character' ` se asegura la relación bidireccional entre Usuario y Character. 

* Atributos de combate: salud, fuerza, defensa, nivel, experiencia representan las estadísticas y progreso del personaje.

* También cabe aclarar que todos los modelos en DJango heredan los campos de su superclase, en este caso de models.Model que ya tiene campos adicionales (por ejemplo el campo id). 	

### Paso 4: Crear el modelo de Objeto (Item). ###

Los objetos son elementos que el personaje puede adquirir o equipar para mejorar sus estadísticas.

* En models.py, añadir el modelo de Item:
	```
	class Item(models.Model):
		nombre = models.CharField(max_length=100)
		descripcion = models.TextField()
		tipo = models.CharField(max_length=50)  # Ejemplo: "arma", "armadura"
		bono_fuerza = models.IntegerField(default=0)
		bono_defensa = models.IntegerField(default=0)
		precio = models.IntegerField(default=50)
		
		def __str__(self):
			return self.nombre
	```
	* tipo: Define el tipo de objeto (ej., arma o armadura).
	* Bonos: bono_fuerza y bono_defensa indican cómo afecta este objeto las estadísticas del personaje.
	* precio: Determina cuánto cuesta adquirir el objeto.

### Paso 5: Crear el modelo de Inventario. ###

* Cada personaje puede tener varios objetos en su inventario por lo cual el modelo tiene que poder permitir esta característica.

* En models.py, añadir el modelo de Inventario:
	```
	class Inventario(models.Model):
		personaje = models.ForeignKey('Character', on_delete=models.CASCADE)
		item = models.ForeignKey(Item, on_delete=models.CASCADE)
		cantidad = models.IntegerField(default=1)
	
		def __str__(self):
			return f"{self.cantidad}x {self.item.nombre} para {self.personaje.nombre}"
	```
	* personaje: Indica a qué personaje pertenece este inventario.
	* item: Define qué objeto está en el inventario.
	* cantidad: Indica cuántos de ese objeto posee el personaje.

### Paso 6: Crear el modelo de Batalla. ###

Para registrar las batallas entre personajes, se crea un modelo que guarda los resultados de cada enfrentamiento.

1. En models.py, añadir el modelo de Battle:
	```
	class Battle(models.Model):
		atacante = models.ForeignKey('Character', related_name="batallas_atacante", null=True, blank=True, on_delete=models.SET_NULL)
		defensor = models.ForeignKey('Character', related_name="batallas_defensor", null=True, blank=True, on_delete=models.SET_NULL)
		ganador = models.ForeignKey('Character', related_name="batallas_ganador", null=True, blank=True, on_delete=models.SET_NULL)
		fecha = models.DateTimeField(auto_now_add=True)
		
		def __str__(self):
			return f"{self.atacante} vs {self.defensor} - Ganador: {self.ganador if self.ganador else 'Empate'}"
	```
	* atacante y defensor: Personajes que participan en la batalla(o pueden ser null si los personajes son borrados del sistema)
	* ganador: Indica el personaje que ganó la batalla (o puede ser null si es un empate).
	* fecha: Fecha y hora de la batalla.

2. Crear signals.py dentro de la carpeta game y colocar el siguiente código:
	```
	from django.db.models.signals import post_delete
	from django.dispatch import receiver
	from .models import Battle, Character
	
	@receiver(post_delete, sender=Character)
	def eliminar_batallas_sin_participantes(sender, instance, **kwargs):
		# Busca batallas sin atacante ni defensor #
		batallas_sin_participantes = Battle.objects.filter(atacante=None, defensor=None)
		# Elimina esas batallas #
		batallas_sin_participantes.delete()
	```
	* Este código es una señal que elimina registros de la tabla Battle sí tanto el atacante como el defensor son eliminados del sistema.

3. En el archiv app.py de game colocar el siguiente código:
	```
	from django.apps import AppConfig
	
	class GameConfig(AppConfig):
		default_auto_field = 'django.db.models.BigAutoField'
		name = 'game'
		
		def ready(self):
			import game.signals  # Importa las señales al cargar la aplicación
	```
	* El siguiente código enlaza la señal con la aplicación para su uso.

### Paso 7: Crear y aplicar las migraciones. ###

1. Ahora que se han definido los modelos, Django necesita crear las tablas correspondientes en MySQL. Primero, generar las migraciones ejecutando:
	```
	python manage.py makemigrations
	```
	Este comando crea los archivos de migración para los modelos que se acaban de definir.

2. Luego, aplicar las migraciones a la base de datos:
	```
	python manage.py migrate
	```
	Esto creará las tablas en la base de datos MySQL basadas en los modelos definidos en models.py.

### Paso 8: Verificar los modelos en el panel de administración de Django. ###

Django incluye un panel de administración que facilita ver y gestionar los datos.

1. En admin.py dentro de la carpeta game, registrar los modelos para que se muestren en el panel de administración:
	```
	from django.contrib import admin
	from .models import Usuario, Character, Item, Inventario, Battle
	
	admin.site.register(Usuario)
	admin.site.register(Character)
	admin.site.register(Item)
	admin.site.register(Inventario)
	admin.site.register(Battle)
	```

2. Crear un superusuario para acceder al panel de administración:
	```
	python manage.py createsuperuser
	```
	Seguir las indicaciones para configurar el nombre de usuario, correo electrónico y contraseña.

3. Iniciar el servidor ` python manage.py runserver ` de desarrollo y acceder al panel de administración en http://127.0.0.1:8000/admin. Iniciar sesión con el superusuario y revisar los modelos registrados en el panel de administración.

---------------------------------------------------------------------
---------------------------------------------------------------------

## Parte 4: Crear Vistas y Rutas Básicas en Django. ##

### Objetivo: ###

Crear vistas y rutas que permitan a los usuarios:

* Ver el perfil de su personaje.

* Consultar su inventario.

* Llevar a cabo una batalla entre personajes.

### Paso 1: Configurar las URLs de la Aplicación game. ###

Para organizar las rutas, se empezará creando un archivo de URL específico para la aplicación game:

1. Dentro de la carpeta game, crear un archivo llamado urls.py.

2. En urls.py, definir las rutas que se van a usar inicialmente:
	```
	from django.urls import path
	from . import views
	
	urlpatterns = [
		path('perfil/', views.perfil_personaje, name='perfil_personaje'),
		path('inventario/', views.inventario, name='inventario'),
		path('batalla/', views.batalla, name='batalla'),
	]
	```
	* perfil/: Ruta para ver el perfil del personaje.
	* inventario/: Ruta para ver el inventario del personaje.
	* batalla/: Ruta para llevar a cabo una batalla.	

3. Luego, incluir estas rutas en la configuración principal de URLs del proyecto. Ir al archivo urls.py en la carpeta principal del proyecto y añadir la ruta para game:
	```
	from django.contrib import admin
	from django.urls import path, include
	
	urlpatterns = [
		path('admin/', admin.site.urls),
		path('game/', include('game.urls')),
	] 
	```
	Con esta configuración, las rutas quedarán accesibles como /game/perfil/, /game/inventario/, y /game/batalla/.

### Paso 2: Crear las Vistas en views.py. ###

Crear las vistas en views.py dentro de la aplicación game.

1. Vista del Perfil del Personaje.

	La vista mostrará la información del personaje del usuario. 

	En views.py, añadir el siguiente código:
	```
	from django.shortcuts import render, get_object_or_404
	from django.contrib.auth.decorators import login_required
	from .models import Character
	
	@login_required
	def perfil_personaje(request):
		# Obtener el personaje del usuario #
		personaje = get_object_or_404(Character, usuario=request.user)
		return render(request, 'game/perfil.html', {'personaje': personaje})
	```
	* @login_required: Restringe el acceso a la vista solo para usuarios autenticados.
	* get_object_or_404: Obtiene el personaje del usuario actual o muestra un error si no se encuentra.

2. Vista del Inventario.

	La vista del inventario mostrará los objetos que posee el personaje.
   
	En views.py, añadir la siguiente función:
	```
	from .models import Inventario
	
	@login_required
	def inventario(request):
		personaje = get_object_or_404(Character, usuario=request.user)
		inventario = Inventario.objects.filter(personaje=personaje)
		return render(request, 'game/inventario.html', {'inventario': inventario, 'personaje': personaje})
	```
	* Inventario.objects.filter(personaje=personaje): Obtiene todos los objetos que el personaje tiene en su inventario.

3. Vista de Batalla.

	Esta vista permite simular una batalla entre el personaje del usuario y otro personaje.

	Añadir esta función en views.py:
	```
	from django.http import HttpResponseRedirect
	from django.urls import reverse
	import random
    	
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
	```
	* Character.objects.exclude(usuario=request.user).order_by('?').first(): Selecciona un enemigo al azar entre los personajes que no son del usuario actual.
	* Resultado de batalla: Se usa random.choice() para decidir aleatoriamente el resultado de la batalla.

### Paso 3: Crear las Plantillas HTML. ###

Crear las plantillas HTML para visualizar el perfil del personaje, el inventario, y el resultado de la batalla.

* Crear una carpeta llamada templates dentro de la carpeta game, y dentro de esta, una subcarpeta llamada game. Colocar las siguientes plantillas dentro de game/templates/game.

1. Plantilla de Perfil del Personaje (perfil.html)
	```
	<!-- perfil.html -->
	<h1>Perfil de {{ personaje.nombre }}</h1>
	<p>Salud: {{ personaje.salud }}</p>
	<p>Fuerza: {{ personaje.fuerza }}</p>
	<p>Defensa: {{ personaje.defensa }}</p>
	<p>Nivel: {{ personaje.nivel }}</p>
	<p>Experiencia: {{ personaje.experiencia }}</p>
	<p>Oro: {{ personaje.oro }}</p>
	<a href="{% url 'inventario' %}">Ver Inventario</a>
	<a href="{% url 'batalla' %}">Ir a Batalla</a>
	```
   
2. Plantilla del Inventario (inventario.html)
	```
	<!-- inventario.html -->
	<h1>Inventario de {{ personaje.nombre }}</h1>
	<ul>
		{% for item in inventario %}
			<li>{{ item.cantidad }}x {{ item.item.nombre }} ({{ item.item.descripcion }})</li>
		{% endfor %}
	</ul>
	<a href="{% url 'perfil_personaje' %}">Volver al Perfil</a>
	```

3. Plantilla de Batalla (batalla.html)
	```
	<!-- batalla.html -->
	<h1>Batalla entre {{ personaje.nombre }} y {{ enemigo.nombre }}</h1>
	<p>Resultado: {{ resultado }}</p>
	{% if resultado == 'victoria' %}
		<p>¡Has ganado! Experiencia y oro aumentados.</p>
	{% else %}
		<p>Has sido derrotado.</p>
	{% endif %}
	<a href="{% url 'perfil_personaje' %}">Volver al Perfil</a>
	```

### Paso 4: Probar las Vistas en el Navegador. ###

1. Iniciar el servidor de desarrollo:
	```
	python manage.py runserver
	```

2. Iniciar sesión con el superusuario http://127.0.0.1:8000/admin.

3. Crear un usuario y dos characters para relacionar (Uno con el superusuario y otro con un usuario normal) en la base de datos de Django.

4. Acceder a http://127.0.0.1:8000/game/perfil/ para ver el perfil del personaje.

5. Desde el perfil, usar los enlaces para navegar al inventario y a la batalla y verifica que todo esté funcionando correctamente.

---------------------------------------------------------------------
---------------------------------------------------------------------

## Parte 5: Mejorar Lógica de Batalla y Sistema de Nivelación. ##

### Objetivo: ###

* Mejorar la lógica de batalla para que sea más detallada y realista.

* Implementar un sistema de progresión para que el personaje suba de nivel cuando acumule suficiente experiencia.

* Añadir mejoras visuales en las plantillas de batalla para mostrar más información sobre el combate.

### Paso 1: Mejorar la Lógica de Batalla. ###

En el paso anterior, la lógica de batalla se decidía al azar. Ahora se implementará una mecánica más detallada en la que se tome en cuenta la fuerza y la defensa de cada personaje. 

1. Mejorar en views.py la función batalla para que el combate sea más complejo.

	Actualiza la función batalla en views.py de la siguiente manera:
	```
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
	```
#### Explicación del Código: ####

* Se calcula el poder de ataque del personaje y el enemigo considerando su fuerza y la defensa del oponente.
* La batalla se realiza en turnos. En cada turno, personaje y enemigo reciben daño.
* Si el personaje gana, se le otorgan experiencia y oro adicionales. Si pierde, su salud se reduce, pero se asegura que nunca llegue a cero (esto puede modificarse).

### Paso 2: Implementar el Sistema de Nivelación. ###

Para hacer que el personaje suba de nivel cuando alcanza cierta cantidad de experiencia, se creará un sistema básico de niveles.

1. Ir al modelo Character en models.py y asegúrase de tener los siguientes campos:
	```
	nivel = models.IntegerField(default=1)
	experiencia = models.IntegerField(default=0)
	experiencia_necesaria = models.IntegerField(default=100)
	```
	* Recordar hacer la migración antes de abrir el server.

2. Modificar el método de batalla para que el personaje suba de nivel automáticamente cuando alcance suficiente experiencia. Se añadirá una función llamada subir_nivel en el modelo Character:
	```
	def subir_nivel(self):
		if self.experiencia >= self.experiencia_necesaria:
			self.nivel += 1
			self.experiencia -= self.experiencia_necesaria
			self.experiencia_necesaria += 50  # Incrementa la experiencia necesaria en cada nivel
			self.salud += 10  # Aumenta la salud
			self.fuerza += 2  # Aumenta la fuerza
			self.defensa += 1  # Aumenta la defensa
			self.save()
	```

3. Luego, llamar a subir_nivel después de actualizar la experiencia del personaje en la función batalla de views.py:
```
if resultado == 'victoria':
	personaje.experiencia += 20
	personaje.oro += 10
	personaje.subir_nivel()
```

### Paso 3: Actualizar la Plantilla de Batalla para Mostrar Más Información. ###

Se actualizará la plantilla batalla.html para mostrar más detalles sobre la batalla y la progresión del personaje.

* Abrir batalla.html en la carpeta templates/game y actualizarla de la siguiente manera:
	```
	<h1>Batalla entre {{ personaje.nombre }} y {{ enemigo.nombre }}</h1>
	<p><strong>Resultado:</strong> {{ resultado }}</p>
	<h2>Registro de Combate</h2> 
	<ul> {% for evento in log_combate %} 
		<li>{{ evento }}</li> 
	{% endfor %} </ul>
	<h2>Estado Final del Combate</h2>
	<p>{{ personaje.nombre }} - Salud: {{ personaje.salud }} | Fuerza: {{ personaje.fuerza }} | Defensa: {{ personaje.defensa }} | Nivel: {{ personaje.nivel }}</p>
	<p>{{ enemigo.nombre }} - Salud: {{ enemigo.salud }} | Fuerza: {{ enemigo.fuerza }} | Defensa: {{ enemigo.defensa }}</p>
	{% if resultado == 'victoria' %}
		<p>¡Has ganado! Experiencia ganada: 20 puntos. Oro ganado: 10.</p>
		<p>Nueva Experiencia: {{ personaje.experiencia }} / {{ personaje.experiencia_necesaria }}</p>
		<p>Nivel: {{ personaje.nivel }}</p>
	{% else %}
		<p>Has sido derrotado. Vuelve a intentarlo.</p>
	{% endif %}
	<a href="{% url 'perfil_personaje' %}">Volver al Perfil</a>
	```
#### En esta plantilla: ####

* Se muestra el estado final del personaje y el enemigo.
* Si el personaje gana, se actualizan los puntos de experiencia y oro.
* El progreso hacia el siguiente nivel se muestra en la sección de experiencia.

### Paso 4: Probar el Sistema de Batalla y Nivelación. ###

1. Ejecutar el Servidor y acceder a la batalla nuevamente:
	```
	python manage.py runserver
	```

2. En la interfaz de usuario, navegar a /game/batalla/ y verifica que:
	* La batalla muestra el daño infligido por cada personaje.
	* El personaje sube de nivel automáticamente al alcanzar la experiencia necesaria.
	* Los atributos del personaje, como salud, fuerza y defensa, aumentan al subir de nivel.

---------------------------------------------------------------------
---------------------------------------------------------------------

## Parte 6: Implementación del Sistema de Misiones. ##

### Objetivo: ###

* Crear un modelo de "Misión" para definir tareas que el jugador puede completar.

* Implementar la lógica para que el jugador pueda aceptar, completar y recibir recompensas por misiones.

* Mejorar las plantillas para mostrar las misiones disponibles, el progreso de las misiones activas y las recompensas obtenidas.

### Paso 1: Crear el Modelo de Misión. ###

En primer lugar, definiremos un nuevo modelo en Django para representar las misiones en el juego.

* Abre models.py en la aplicación game y añade el siguiente código:
	```
	from django.db import models
	from django.contrib.auth.models import User
	
	class Mision(models.Model):
		nombre = models.CharField(max_length=100)
		descripcion = models.TextField()
		recompensa_experiencia = models.IntegerField()
		recompensa_oro = models.IntegerField()
		completada = models.BooleanField(default=False)
	
	def __str__(self):
		return self.nombre
	
	class MisionActiva(models.Model):
		usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
		mision = models.ForeignKey('Mision', on_delete=models.CASCADE)
		progreso = models.IntegerField(default=0)
		completada = models.BooleanField(default=False)
	
	def __str__(self):
		return f"{self.usuario.username} - {self.mision.nombre}"
	```
#### Explicación del Código: ####

* Mision define las características básicas de una misión: el nombre, la descripción y las recompensas (experiencia y oro).
* MisiónActiva asocia una misión con un jugador (`usuario`) y almacena su progreso y estado de completitud. 
* Ejecuta las migraciones para actualizar la base de datos con los nuevos modelos:
	```
	python manage.py makemigrations
	python manage.py migrate
	```

### Paso 2: Crear Misiones Iniciales en el Panel de Administración. ###

Ahora que tenemos el modelo de Mision, vamos a crear algunas misiones iniciales.

1. En admin.py, añade los nuevos modelos para poder gestionarlos desde el panel de administración:
	```
	from django.contrib import admin
	from .models import Mision, MisionActiva
	
	admin.site.register(Mision)
	admin.site.register(MisionActiva)
	``` 

2. Ve al panel de administración de Django en http://127.0.0.1:8000/admin, y añade algunas misiones de prueba con diferentes recompensas.

### Paso 3: Crear Vistas para las Misiones. ###

Ahora, crearemos las vistas que permitirán al usuario ver las misiones disponibles, aceptar una misión, y completar misiones para obtener recompensas.

* En views.py, añade la lógica para las misiones:
	```
	from django.shortcuts import render, get_object_or_404, redirect
	from .models import Mision, MisionActiva
	from django.contrib.auth.decorators import login_required
	
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
	def completar_mision(request, mision_activa_id):
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
	```
#### Explicación del Código: ####

* misiones_disponibles: Muestra las misiones que el jugador puede aceptar.
* aceptar_mision: Permite que el jugador acepte una misión disponible.
* completar_mision: Marca una misión como completada y otorga al jugador las recompensas de experiencia y oro.

### Paso 4: Crear Plantillas para las Misiones. ###

Para que el usuario pueda interactuar con las misiones, vamos a crear las plantillas misiones_disponibles.html y perfil_personaje.html en la carpeta templates/game.

1. En templates/game/misiones_disponibles.html, añade el siguiente código:
	```
	<h1>Misiones Disponibles</h1>
    <ul>{% for mision in misiones %}
        {% if not mision in misiones_activas_completas %}
            <li>
                <h3>{{ mision.nombre }}</h3>
                <p>{{ mision.descripcion }}</p>
                <p>Recompensa: {{ mision.recompensa_experiencia }} experiencia, {{ mision.recompensa_oro }} oro</p>
                {% if not mision in misiones_activas %}
                    <a href="{% url 'aceptar_mision' mision.id %}">Aceptar Misión</a>
                {% else %}
                    <a href="{% url 'completar_mision' mision.id %}">Completar Misión</a>
                {% endif %}
            </li>
        {% endif %}
    {% endfor %}</ul>
    <hr>
    <a href="{% url 'perfil_personaje' %}">Volver al perfil</a>
	```

2. En urls.py, añade las rutas para estas vistas de misiones:
	```
	from django.urls import path
	from . import views
	
	urlpatterns = [
		path('misiones/', views.misiones_disponibles, name='misiones_disponibles'),
		path('misiones/aceptar/<int:mision_id>/', views.aceptar_mision, name='aceptar_mision'),
		path('misiones/completar/<int:mision_id>/', views.completar_mision, name='completar_mision'),
		path('perfil/', views.perfil_personaje, name='perfil_personaje'),
	]
	```

3. Paso extra, agregar el enlace a las misiones en perfil.html:
	```
	<a href="{% url 'misiones_disponibles' %}">Misiones</a>
	```

### Paso 5: Probar el Sistema de Misiones. ###

1. Ejecuta el Servidor y navega a la página de misiones en http://127.0.0.1:8000/game/misiones/.

2. Prueba el flujo:
	* Acepta una misión haciendo clic en "Aceptar Misión".
	* Una vez aceptada, vuelve a la lista de misiones, y ahora verás la opción "Completar Misión".
	* Completa la misión para recibir las recompensas de experiencia y oro.
	* Navega al perfil del personaje para ver si la experiencia y el oro se han actualizado correctamente.

---------------------------------------------------------------------
---------------------------------------------------------------------

