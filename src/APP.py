from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

"""NOTA PARA EL DESARROLLADOR: En este proyecto utiliza la clase llamada Task
esta razon es porque no realiza las funciones de GET muestra el Json vacio"""

#Creacion de la APP
app = Flask(__name__)

#Conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/usuarios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

BaseDatos = SQLAlchemy(app)
#*************************
Marcelo = Marshmallow(app)
#Marcelo agachate y conocelo *BeatBox Perron*
#*************************

#Creamos la tarea en base al modelo de la Base de datos
class Task(BaseDatos.Model):
    id = BaseDatos.Column(BaseDatos.Integer, primary_key = True)
    Nombre = BaseDatos.Column(BaseDatos.String(30))
    Edad =  BaseDatos.Column(BaseDatos.Integer)
    Ciudad = BaseDatos.Column(BaseDatos.String(30))
    
    def __init__(self, Nombre, Edad, Ciudad):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Ciudad = Ciudad

#Creado la base de datos
BaseDatos.create_all()

class TaskSchema (Marcelo.Schema):
    class Meta:
        fields = ('id', 'Nombre', 'Edad', 'Ciudad')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

#Creacion de las rutas
#Mostrar datos
@app.route('/Usu')
def GETusuarios():
    AllUsuarios = Task.query.all()
    UsuariosRelut = tasks_schema.dump(AllUsuarios)
    return jsonify(UsuariosRelut)

#Mostrar un solo ususario
@app.route('/Usu/<id>')
#En esta funcion dentro de los parametros ingresaremos el ID
def GETusuario(id):
    Identificador = Task.query.get(id)
    return task_schema.jsonify(Identificador)

#Enviar datos
@app.route('/Usu', methods = ['POST'])
def POSTusuario():
    #Enviar los datos y guardalos en nuestro BD
    Nombre = request.json['Nombre']
    Edad = request.json['Edad']
    Ciudad = request.json['Ciudad']

    NuevoUsuario = Task(Nombre, Edad, Ciudad)
    BaseDatos.session.add(NuevoUsuario)
    BaseDatos.session.commit()

    #Confirmacion
    return task_schema.jsonify(NuevoUsuario)

#Actualizar datos
@app.route('/Usu/<id>', methods = ['PUT'])
def PUTusuario(id):
    IndiPUT =  Task.query.get(id)

    #Datos a actualizar
    Nombre = request.json['Nombre']
    Edad =  request.json['Edad']
    Ciudad = request.json['Ciudad']

    #Proceso de actualizacion
    IndiPUT.Nombre = Nombre
    IndiPUT.Edad = Edad
    IndiPUT.Ciudad = Ciudad

    #Guardar
    BaseDatos.session.commit()
    return task_schema.jsonify(IndiPUT)

#Elimiar un registro
@app.route('/Usu/<id>', methods = ['DELETE'])
def DELETEusuario(id):
    indiDELETE = Task.query.get(id)
    BaseDatos.session.delete(indiDELETE)
    BaseDatos.session.commit()

    #Confirmacion
    return task_schema.jsonify(indiDELETE)

#Instrucciones sobre las rutas de los datos Json
@app.route('/')
def Inicio():
    return jsonify({
        'Inicio': 'Este es un API hecha con FLASK',
        'Ver usuarios': 'Para ver los usuarios ingresa la url: http://localhost:5000/Usu',
        'Ver solamente un usuario': 'Solamente el mismo url pero con el ID ejemplo http://localhost:5000/Usu/1',
        'Nota': 'Los ID estan conformados de numeros',
        'Codigo': 'https://github.com/AngelSosaGonzalez/APIMySQLFlask',
        'Creditos': 'Fazt: https://www.youtube.com/watch?v=MvVqjQqSdM4&t=936s'
    })

#Iniciacion del servicio
if __name__ == "__main__":
    app.run(debug=True)