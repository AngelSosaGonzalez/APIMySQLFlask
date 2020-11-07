# APIMySQLFlask
Esta API hecha con Python utilizando el Framework llamado Flask, es una continuación de un anterior proyecto hecho, el punto de este proyecto es enviar, consultar y borrar registros en base a archivos json (que básicamente ya es considerado un API de tipo REST). 

# Antes de iniciar

Usaremos VSCode (Puedes usar la que tu quieras)
- Link: https://code.visualstudio.com/download

Para este proyecto como usaremos MySQL instalaremos XAMPP
- Link: https://sourceforge.net/projects/xampp/files/latest/download (O en su pagina oficial)

Como API la probaremos con el programa POSTMAN igual podemos usar Insomnia pero pues POSTMAN ya lo tengo decargado
Dejos los links de las dos:

POSTMAN
- Link: https://www.postman.com/downloads/

Insomnia
- Link: https://insomnia.rest/download/ 

Instalar el framework:
- Comando: pip install flask

Instalar las dependencias del framework (Las conexiones con la BD)
- Comandos:
- pip install flask-sqlalchemy
- pip install flask-marshmallow 
- pip install marshmallow-sqlalchemy

Instalar los drivers se MySQL
- Comando: pip install pymysql

Ejecutar el proyecto
- python src/APP.py

# AH PROGRAMAR!!!

# NOTA (ACTUALIZADA): Este proyecto se realizo en un entorno virtual

Instalar el entorno virtual
- Comando: pip install virtualenv

Ya instalado el entorno vamos a crear uno
- Insertamos comando: virtualenv *El nombre de nuestro entorno*
- Ejecutaremos en la terminal de nuestro editor el proceso por lotes llamada "activate.bat"
- .\*nombre del entorno*\Scripts\activate.bat

# AHORA SI A PROGRAMAR!!!

# creditos: https://www.youtube.com/watch?v=MvVqjQqSdM4&t=936s 
