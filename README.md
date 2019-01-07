# django-channels
Implemetación de chat con los channels de python

# Instalar Requisitos

mkvirtualenv channels

pip install -r requeriments.txt

sudo apt-get install redis-server

Para instalar la apliacacion en modo desarrollo debera seguir los siguientes pasos:
===========================================================

1-) Instalar el controlador de versiones git:
------------------------------------------------------
    
    Ingresar como super usuario:

    $ su

    # aptitude install git
    
    Salir del modo super usuario

2-) Descargar el codigo fuente del proyecto django_chat_and_notification :
-------------------------------------------------------------------------------------------------

    Para descargar el código fuente del proyecto contenido en su repositorio GIT realice un clon del proyecto django-channels:

    $ git clone https://github.com/rudmanmrrod/django-channels.git

3-) Crear un Ambiente Virtual:
---------------------------------------

    El proyecto está desarrollado con el lenguaje de programación Python, se debe instalar Python v3.4.2. Con los siguientes comandos puede instalar Python y PIP.

    Entrar como root o super usaurio para la instalacion 

    # aptitude install python3.4 python3-pip python3.4-dev python3-setuptools

    # aptitude install python3-virtualenv virtualenvwrapper

    Salir del modo root y crear el ambiente:

    $ mkvirtualenv --python=/usr/bin/python3 django-channels

4-) Instalar los requerimientos del proyecto:
---------------------------------------------------------

    Para activar el ambiente virtual django-channels ejecute el siguiente comando:

    $ workon django-channels

    Con el comando anterio se activa el ambiente virtual quedando de la siguiente manera:

    (django-channels)$

    Entrar en la carpeta raiz del proyecto:

    (django-channels)$ cd django-channels

    (django-channels)django-channels$ 

    Desde ahi se deben instalar los requirimientos del proyecto con el siguiente comando:

    (django-channels)$ pip install -r requirements.txt

    De esta manera se instalaran todos los requerimientos iniciales para montar el proyecto 
    
5-) Instalar Redis:
---------------------------------------------------------

    Para tener un layer para los channels es necesario instalar redis:

    sudo apt-get install redis-server

    Probar que el cliente esta funcionando

    redis-cli ping
    PONG

6-) Crear base de datos y Migrar los modelos:
------------------------------------------------------------

    El manejador de base de datos que usa el proyecto es SQLite3.

    Para migrar los modelos del proyecto se debe usar el siguiente comando:

    (django_chat_and_notification)$ python manage.py makemigrations

    (django_chat_and_notification)$ python manage.py makemigrations chat

    (django_chat_and_notification)$ python manage.py makemigrations notification

    (django_chat_and_notification)$ python manage.py migrate


6.1-) Realizar la instalacion de la data incial del proyecto:
-------------------------------------------------------------------------

    (django_chat_and_notification)$ python manage.py loaddata fixtures/initial_data_tipo_notificacion.json 

7-) Instalar las dependencias de nodejs para el uso del socket.io:
------------------------------------------------------------------------------------

    Asegurece de tener instalada la ultima version de node.

    Si no la posee puede iniciar la instalación siguiendo los pasos que describe el siguiente enlace:

    https://rukbottoland.com/blog/como-instalar-node-js-y-npm/

    Una vez instlado se ingresa al directorio raiz del proyecto y entramos al modulo node_chatnot:  ruta ->  django_chat_and_notification/node_chatnot, en ese subdirectorio ingresamos el siguiente comando para instalar los paquetes que sera usado por el modulo de nodeJs:

    $ npm install

    Salir del subdirectorio y entrar en el directorio raiz del proyecto.

8-) Correr la aplicacion django_chat_and_notification:
------------------------------------------------------------------------------

    Para correr la apliacion se debe  ejecutar el siguiente comando:

    (django_chat_and_notification)$ python manage.py runserver

    Ingresar a la plataforma en la ruta: localhost:8000

    Para correr el socket.io que escucha los eventos del chat, debemos abrir otra consola ingresar al directorio raiz del proyecto ubicarse en el modulo  node_chatnot e insertar el siguiente comando:

    $node server.js

    Esto ejecutara un servidor de escucha en el puerto 3000


Estandar de desarrollo del proyecto:
=============================

1-) Documentación:
----------------------------

    El proyecto se encuentra documentado bajo la Convenciones  la PEP257 Docstring Conventions

    Leer el siguiente elace para su aplicación:

    https://www.python.org/dev/peps/pep-0257/

2-) Codificación:
----------------------

    El proyecto se encuentra codificado bajo la Guía de estilo para el código Python PEP8

    Leer el siguiente elace para su aplicación:

    https://www.python.org/dev/peps/pep-0008/