import re
from sqlite3.dbapi2 import SQLITE_CREATE_VIEW
from app import app
from flask import render_template, flash, request, session
from flask.helpers import make_response, url_for
from flask import request
from db.db import consID,consUsuario,insertPersona, insertEmpleado,consIdUser,updatePersona,updateUsuario,eliminarUsuario,eliminarPersona,insertUsuario,consIdEmplo,consUsuarioEmplo
from werkzeug.utils import redirect
import sqlite3
from sqlite3 import Error


@app.route('/adminEmplo')
def adminEmplo():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Gestión de Empleados"
    return render_template("adminEmplo.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje)

@app.route('/funcionEmpleado',methods=['POST'])
def funcionEmpleado():

    operacion=request.form["admon"]

    if operacion=="registroEmpleado":
        #redirect(url_for --> Revisar como se utiliza?
        return redirect(url_for("crearEmpleado"))
    elif operacion=="editarEmpleado":
        return redirect(url_for("index"))
    elif operacion=="visualizarEmpleado":
        return redirect(url_for("index"))
    elif operacion=="desempeno":
        return redirect(url_for("desempeno"))
    elif operacion=="listaEmpleados":
        return redirect(url_for("listaEmpleados"))
    

@app.route('/desempeno')
def desempeno():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Gestor de Empleados"

    return render_template('desempeno.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje)

@app.route('/crearEmpleado')
def crearEmpleado():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Crear Empleado"

    return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje)

@app.route('/actualizarDesempeno/',methods=['POST'])
def actualizarDesempeno():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Gestor de Empleados"

    id=request.form['id']
    user=request.form['user']

    suma_Id=sum(c != ' ' for c in id)
    suma_User=sum(c != ' ' for c in user)

    if(suma_Id>0):
        consId=consIdEmplo(id)
        if(len(consId)>0):
            consPersona=consIdEmplo(consId[0][0])
            ide=str(consId[0][0])
            name=consId[0][1]
            
        
            return render_template('desempeno.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,user=user)
        else:
            flash("Identificación no encontrada")
            return render_template('desempeno.html',class1=class1,class2=class2,class3=class3)

    #Revisar error en busqueda por limite de lista, cuál está llamando?
    elif(suma_User>0):
        consUser=consUsuarioEmplo(user)
        #print('*********************************************',consUser)
        if(len(consUser)>0):
            consPersona=consUsuarioEmplo(consUser[0][1])
            print('*********************************************',consUser[0][1])
            ide=str(consPersona[0][0])
            name=consPersona[0][1]
            user=consUser[0][1]
            
            
            return render_template('desempeno.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,user=user)
        else:
            flash("Empleado no registrado")
            return render_template('desempeno.html',class1=class1,class2=class2,class3=class3)
    else:
        flash("Ingrese los datos correctamente")
        return render_template('desempeno.html',class1=class1,class2=class2,class3=class3)


@app.route('/EmpleadoUser/',methods=['POST'])
def EmpleadoUser():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Gestor de Empleados"

    id=request.form['id']
    user=request.form['user']

    suma_Id=sum(c != ' ' for c in id)
    suma_User=sum(c != ' ' for c in user)

    if(suma_Id>0):
        consId=consID(id)
        if(len(consId)>0):
            consPersona=consIdUser(consId[0][0])
            ide=str(consId[0][0])
            name=consId[0][1]
            gender=consId[0][2]
            address=consId[0][3]
            user=consPersona[0][1]
        
            return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,user=user, gender=gender, address=address)
        else:
            flash("Identificación no encontrada")
            return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3)

    elif(suma_User>0):
        consUser=consUsuario(user)
        if(len(consUser)>0):
            consPersona=consID(consUser[0][0])
            ide=str(consPersona[0][0])
            name=consPersona[0][1]
            user=consUser[0][1]
            gender=consPersona[0][2]
            address=consPersona[0][3]
            
            return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,user=user,gender=gender,address=address)
        else:
            flash("Empleado no registrado")
            return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3)
    else:
        flash("Empleado no registrado")
        return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3)


@app.route('/registroNuevoEmpleado')
def registroNuevoEmpleado():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Registro de Empleados"
    return render_template("registroNuevoEmpleado.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje)

@app.route('/listaEmpleados')
def listaEmpleados():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Visualización Empleados Registrados"
    return render_template("listaEmpleados.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje)


@app.route('/validarRegistroEmpleado/',methods=["POST"])
def validarRegistroEmpleado():
    id=request.form['id']
    user=request.form['user']
    name=request.form['name']
    gender=request.form['gender']
    address=request.form['address']
    cargo=request.form['cargo']
    departamento=request.form['departamento']
    salario=request.form['salario']
    frecuencia=request.form['frecuencia']
    contract=request.form['contrato']
    fechaInicio=request.form['fechaInicio']
    fechaTermino=request.form['fechaTermino']
    password=request.form['password']
    permisos=request.form['permiso']

    persona=len(consID(id))

    if(persona>0):
        flash("Cedula ya registrada. Complemente la información")
        return redirect('/crearEmpleado')
    else:
        usuario=len(consUsuario(user))

        if(usuario>0):
            flash("Usuario ya registrado. Complemente la información")
            return redirect('/crearEmpleado')
        else:
            insertPersona(id,name,gender,address)
            insertEmpleado(id,user,name, gender, address, cargo, departamento, salario, frecuencia, contract, fechaInicio,fechaTermino,password,permisos)
            insertUsuario(id,user,password,permisos)
            flash("Empleado registrado")
            #return str(id)+user+name+gender+address+cargo+departamento+salario+frecuencia+contract+fechaInicio+fechaTermino
            return redirect('/registroNuevoEmpleado')

@app.route('/consultaEmpleados')
def consultaEmpleados():
    
    try:
        con=sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        cur=con.cursor()
        cur.execute('SELECT * FROM empleados ORDER by usuario')
    #MOSTRAMOS TABLA
        rows = cur.fetchall()
        
        return render_template("listaEmpleados.html", rows=rows)
    except Error as err:
        return err


    