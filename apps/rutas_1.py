import re
from app import app
from flask.helpers import make_response, url_for
from flask import render_template, flash, request, session
from flask.wrappers import Request
from flask import request
from db.db import consID,consUsuario,insertPersona,insertUsuario,consUsuarioPassword,consIdUser,updatePersona,updateUsuario,eliminarUsuario,eliminarPersona,consultarAllUsuario,consultarAllPersona,insertEmpleado
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash


@app.errorhandler(404)
def page_not_found(e):#Esta función debe recibir el error como parametor, e es el error
    class1="nav-link active"
    class2="nav-link "
    class3="nav-link "
    mensaje="Error en la busqueda"
    return render_template("errorCarga.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje)

@app.route('/')
def index():
    #session.clear() esta linea elimina las sessiones como los mensajes flash !!
    class1="nav-link active"
    class2="nav-link "
    class3="nav-link "
    mensaje="Inicio Sesión"

    return render_template("iniciarSesion.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje)


@app.route('/funcionActividad',methods=["POST"])
def funcionActividad():

    operacion=request.form["actividad"]

    if operacion=="inicioSesion":
        session.clear()
        return redirect("/")
    elif operacion=="adminUser":
        return redirect("/gestorUsuario")
    elif operacion=="allUsers":
        return redirect("/allUsuarios/")
    elif operacion=="adminEmplo":
        return redirect("/adminEmplo")
    else:
        return redirect(404)


@app.route('/usuarioInicio')
def usuarioInicio():
    if session.get('usuario'):
        class1="nav-link active"
        class2="nav-link "
        class3="nav-link "
        mensaje="Bienvenido "+session['usuario']
        #mensaje="Bienvenido usuario"
        return render_template("usuarioInicio.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
    else:
        flash('Inicie primero sesión','info')
        return redirect(url_for('index'))
        #return render_template("iniciarSesion.html")

@app.route('/registrarUsuario')
def registrarUsuario():
    class1="nav-link active"
    class2="nav-link "
    class3="nav-link "
    mensaje="Registro de Usuario"
    return render_template("registroUsuario.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje)

@app.route('/gestorUsuario')
def gestorUsuario():

    if (session.get('usuario')):
        if(session['permisos']=="adminUser"):
            class1="nav-link"
            class2="nav-link active"
            class3="nav-link"
            mensaje="Bienvenido "+session["usuario"]
        #mensaje="Gestor de usuarios"
            return render_template("gestorUsuarios.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
        else:
            class1="nav-link active"
            class2="nav-link "
            class3="nav-link "
            flash("No puede acceder al gestor de usuarios")
            mensaje="Bienvenido "+session["usuario"]
            return render_template("usuarioInicio.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
    else:
        flash('Inicie primero sesión','info')
        return redirect(url_for('index'))


@app.route('/validarRegistro/',methods=["POST"])
def validarRegistro():
    id=request.form['id']
    name=request.form['nombre']
    genero=request.form['genero']
    address=request.form['address']
    user=request.form['user']
    password=request.form['password']
    permisos=request.form['permiso']
    #return permisos+id+name+genero+address+user+password

    persona=len(consID(id))

    if(persona>0):
        flash("Cedula ya registrada")
        return redirect('/registrarUsuario')
    else:
        usuario=len(consUsuario(user))

        if(usuario>0):
            flash("Usuario ya registrada")
            return redirect('/registrarUsuario')
        else:
            password=generate_password_hash(password)
            insertPersona(id,name,genero,address)
            insertUsuario(id,user,password,permisos)
            flash("Usuario registrado")
            return redirect('/registrarUsuario')
           
@app.route('/inicioSesion/', methods=["POST"])
def inicioSesion():
    user=request.form['user']
    password=request.form['password']
    userData=consUsuarioPassword(user)

    if len(userData)==0: #Si userData no tiene usuarios es por que ingreso mal el usuario.
        flash("Usuario incorrecto")
        return redirect('/')
    else:
        passwordDB=userData[0][2]
        if(check_password_hash(passwordDB,password)):
            #permisos=userData[0][3]
            session.clear()
            session['id']=userData[0][0]
            session['usuario']=userData[0][1]
            session['password']=userData[0][2]
            session['permisos']=userData[0][3]

            if(session['permisos']=="usuario"):
                return redirect('/usuarioInicio')
            elif(session['permisos']=="adminUser"):
                return redirect('/gestorUsuario')
            elif(session['permisos']=="adminEmplo"):
                return "admin empleados"
            else:
                return "Sin permisos"
            
        else:
            flash("contraseña incorrecta")
            return redirect('/')
        
   
@app.route('/consultarUsuario/',methods=['POST'])
def consultarUsuario():
    class1="nav-link"
    class2="nav-link active"
    class3="nav-link"
    mensaje="Gestor de usuario"

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
            password=consPersona[0][2]
            permisos=consPersona[0][3]
            return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,gender=gender,address=address,user=user,password=password,permisos=permisos,permiso=session['permisos'])
        else:
            flash("Identificación no encontrado")
            return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])

    elif(suma_User>0):
        consUser=consUsuario(user)
        if(len(consUser)>0):
            consPersona=consID(consUser[0][0])
            ide=str(consPersona[0][0])
            name=consPersona[0][1]
            gender=consPersona[0][2]
            address=consPersona[0][3]
            user=consUser[0][1]
            password=consUser[0][2]
            permisos=consUser[0][3]
            return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,ide=ide,name=name,gender=gender,address=address,user=user,password=password,permisos=permisos,permiso=session['permisos'])
        else:
            flash("Usuario no encontrado")
            return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
    else:
        flash("Ingrese los datos correctamente")
        return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])


@app.route('/operacionUsuario/',methods=['POST'])
def operacionUsuario():
    class1="nav-link"
    class2="nav-link active"
    class3="nav-link"
    mensaje="Gestor de usuario"

    ide=request.form['ide']
    name=request.form['name']
    sexo=request.form['gender']
    address=request.form['address']
    user=request.form['user']
    permiso=request.form['permiso']
    password=request.form['password']

    suma_Id=sum(c != ' ' for c in ide)

    if(request.form['submitButton']=="Actualizar"):

        if(suma_Id>0):
            user=consUsuario(user)
            passwordSql=user[0][2]
            if(password==passwordSql):
                updatePersona(name,sexo,address,ide)
                updateUsuario(password,permiso,ide)
                flash("Usuario actualizado")
                return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
            else:
                password=generate_password_hash(password)
                updatePersona(name,sexo,address,ide)
                updateUsuario(password,permiso,ide)
                flash("Usuario actualizado")
                return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
        else:
               flash("Usuario no consultado")
               return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
    elif(request.form['submitButton']=="Eliminar"):
        
        if(suma_Id>0):
            eliminarUsuario(ide)
            eliminarPersona(ide)
            flash("Usuario eliminado")
            return render_template('gestorUsuarios.html',class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
    

    #return str(ide)+name+sexo+address+user+permiso+password #Obteniendo los datos del formulario consultado.

@app.route('/allUsuarios/')
def allUsuarios():

    if (session.get('usuario')):
        if(session['permisos']=="adminUser"):
            class1="nav-link"
            class2="nav-link"
            class3="nav-link active"
            mensaje="Consultar todos los usuarios"
            users=consultarAllUsuario()
            personas=consultarAllPersona()

            datos=[]
            for i in range(len(users)):
                datos.append((personas[i][0],personas[i][1],users[i][1],users[0][3],personas[i][2],personas[i][3],))

            return render_template("allUsuarios.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje,data=datos,permiso=session['permisos'])
        else:
            class1="nav-link active"
            class2="nav-link disabled"
            class3="nav-link disabled"
            flash("No puede acceder a la consulta de los usuarios")
            mensaje="Bienvenido "+session["usuario"]
            return render_template("usuarioInicio.html",class1=class1,class2=class2,class3=class3,mensaje=mensaje,permiso=session['permisos'])
    else:
        flash('Inicie primero sesión','info')
        return redirect(url_for('index'))

