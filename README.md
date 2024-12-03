# Fight_Copy #

Repositorio de prueba para proyecto de diseño web.

---------------------------------------------------------------------
---------------------------------------------------------------------

## Parte 1: Configuración del entorno de desarrollo. ##

### Paso 1: Crear una cuenta en GitHub. ###

* Entrar a https://github.com/, regístrarse y completar el proceso de verificación.
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
	* Descárgar desde https://www.python.org/downloads/ y seguir los pasos de instalación (No olvidarse de marcar la opción de PATH).
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
