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