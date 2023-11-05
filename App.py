from flask import Flask, render_template, request,Response, jsonify, redirect, url_for
import database as dbase
from planilla import Planilla 

db = dbase.dbConnection()

App = Flask(__name__)
#Rutass de la aplicacion
@App.route('/')
def home():
    planillas = db['planillas']
    planillasReceived = planillas.find()
    return render_template('index.html', planillas = planillasReceived)
#Method Post
@App.route('/planillas', methods=['POST'])
def AddEmpleado():    
    planillas = db['planillas']
    codEmpleado = request.form['codEmpleado']
    Nombre = request.form['Nombre']
    Apellido = request.form['Apellido']
    Cargo = request.form['Cargo']
    Correo = request.form['Correo']
    Direccion = request.form['Direccion']
    Salario = request.form['Salario']

    if  codEmpleado and Nombre and Apellido and Cargo and Correo and Direccion and Salario:
        planilla =Planilla (codEmpleado,Nombre,Apellido,Cargo,Correo,Direccion, Salario)
        planillas.insert_one(planilla.toDBCollection())
        response = jsonify({
            'CodEmpleado': codEmpleado,
            'Nombre': Nombre,
            'Apellido': Apellido,
            'Cargo': Cargo,
            'Correo': Correo,
            'Direccion': Direccion,
            'Salario': Salario

        })
        return redirect(url_for('home'))
    else:
        return notFound()
    

#Metodo delete
@App.route('/delete/<string:planilla_CodEmpleado>')
def delete(planilla_CodEmpleado):
    planillas = db['planillas']
    planillas.delete_one({'codEmpleado' : planilla_CodEmpleado})
    return redirect(url_for('home'))

#Metodo Put 
@App.route('/edit/<string:planilla_CodEmpleado>', methods=['POST'])
def edit(planilla_CodEmpleado):
    planillas = db['planillas']
    codEmpleado = request.form['codEmpleado']
    Nombre = request.form['Nombre']
    Apellido = request.form['Apellido']
    Cargo = request.form['Cargo']
    Correo = request.form['Correo']
    Direccion = request.form['Direccion']
    Salario = request.form['Salario']

    if  codEmpleado and Nombre and Apellido and Cargo and Correo and Direccion and Salario:
        planillas.update_one({'codEmpleado' : planilla_CodEmpleado}, {'$set' :{'codEmpleado' : codEmpleado,'Nombre' : Nombre,'Apellido' : Apellido,'Cargo' : Cargo,'Correo' : Correo,'Direccion' : Direccion,'Salario' : Salario}})
        response =jsonify({'message' :'Empleado '+ planilla_CodEmpleado + 'actualizado correctamente'})
        return redirect(url_for('home'))
    
    else: notFound()





@App.errorhandler(404)
def notFound(error=None):
    message={
        'message': 'No encontrado '+ request.url,
        'status': '404 Not Found'

    }    
    response=jsonify(message)
    response.status_code =404
    return response


if __name__=='__main__':
    App.run(debug=True, port=4000)
