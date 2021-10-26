from app import app
from flask import render_template, flash, request, session
from db.db import consID,consUsuario,insertEmpleado,consIdUser,updatePersona,updateUsuario,eliminarUsuario,eliminarPersona
from werkzeug.utils import redirect



@app.route('/adminEmplo')
def adminEmplo():
    class1="nav-link"
    class2="nav-link"
    class3="nav-link active"
    mensaje="Gestor de Empleados"
    return render_template("adminEmplo.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje)

@app.route('/funcionAdmonEmpleado',methods=["POST"])
def funcionAdmonEmpleado():

    operacion=request.form["admon"]

    if operacion=="registroEmpleado":
        session.clear()
        return redirect("/crearEmpleado")
    elif operacion=="adminUser":
        return redirect("/desempeno")
    elif operacion=="adminEmplo":
        return redirect("/listaEmpleados")

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
        consId=consID(id)
        if(len(consId)>0):
            consPersona=consIdUser(consId[0][0])
            ide=str(consId[0][0])
            name=consId[0][1]
        
            return render_template('desempeno.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,user=user)
        else:
            flash("Identificación no encontrado")
            return render_template('desempeno.html',class1=class1,class2=class2,class3=class3)

    elif(suma_User>0):
        consUser=consUsuario(user)
        if(len(consUser)>0):
            consPersona=consID(consUser[0][0])
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
            flash("Identificación no encontrado")
            return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3)

    elif(suma_User>0):
        consUser=consUsuario(user)
        if(len(consUser)>0):
            consPersona=consID(consUser[0][0])
            ide=str(consPersona[0][0])
            name=consPersona[0][1]
            user=consUser[0][1]
            
            return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,user=user)
        else:
            flash("Empleado no registrado")
            return render_template('crearEmpleado.html',class1=class1,class2=class2,class3=class3)
    else:
        flash("Ingrese los datos correctamente")
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
