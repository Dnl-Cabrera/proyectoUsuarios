from os import error
import sqlite3
from sqlite3 import Error
import os

#CURR_DIR = os.getcwd() #Obtiene el directorio actual madre
#URL_DB=CURR_DIR+"\proyectoUsuarios\database.db"
URL_DB="database.db"

def get_db():
    try:
        print("RUTA:")
        print(URL_DB)
        con = sqlite3.connect(URL_DB)
        return con
    except :
        print ('error')

def sql_query_registro(id=None,usuario=None):
    try:
        strsql = "select * from registro where id='"+id+"' or usuario='"+usuario+"';"# and correo="+correo+";"
        con = get_db()
        cursorObj = con.cursor() ##el cursor es necesario para realizar cualquier tipo de consultas
        cursorObj.execute(strsql)
        productos = cursorObj.fetchall()
        if(len(productos)>0):
            con.close()
            return False
        else:
            con.close()
            return True
    except Error as err:
        return err

def insertPersona(id,nombre,sexo,direccion):
    try:
        con1=get_db()
        cur1=con1.cursor()
        sqlInsert_persona="INSERT INTO persona(id, nombre, sexo, direccion) VALUEs (?, ?, ?, ?);"
        cur1.execute(sqlInsert_persona,(id,nombre,sexo,direccion))
        con1.commit()
        con1.close()
    except Error as err:
        return err 

def insertUsuario(id,usuario,password,permisos):
    try:
        con1=get_db()
        cur1=con1.cursor()
        sqlInsert_usuario="INSERT INTO usuario(id, usuario, password, permisos) VALUEs (?, ?, ?, ?);"
        cur1.execute(sqlInsert_usuario,(id,usuario,password,permisos))
        con1.commit()
        con1.close()
    except Error as err:
        return err

def consID(id):
    try:
        con1=get_db()
        cur=con1.cursor()
        sql_consulta_persona="select * from persona where id=?;"
        res_persona=cur.execute(sql_consulta_persona,(int(id),)) #Si es solo un dato se debe agregar una coma
        persona = cur.fetchall()
        con1.close()
        return persona
    except Error as err:
        return err

def consIdUser(id):
    try:
        con1=get_db()
        cur=con1.cursor()
        sql_consulta_persona="select * from usuario where id=?;"
        res_persona=cur.execute(sql_consulta_persona,(int(id),)) #Si es solo un dato se debe agregar una coma
        persona = cur.fetchall()
        con1.close()
        return persona
    except Error as err:
        return err

def consUsuario(usuario):
    try:
        con=get_db()
        cur=con.cursor()
        sql_consulta_usuario="select * from usuario where usuario=?"
        res_usuario = cur.execute(sql_consulta_usuario,(usuario,))
        user=cur.fetchall()
        con.close()
        return user
    except Error as err:
        return err


def updatePersona(nombre,sexo,direccion,id):
    try:
        con=get_db()
        cur=con.cursor()
        #sql="UPDATE persona INNER JOIN usuario ON(persona.id = usuario.id) SET persona.nombre = ?, persona.sexo = ?, persona.direccion=?, usuario.password=?, usuario.permisos=? WHERE persona.id = ?;"
        sql="UPDATE persona SET nombre = ?, sexo = ?, direccion=? WHERE id = ?;"
        cur.execute(sql,(nombre,sexo,direccion,id))
        con.commit()
        con.close()
        return True
    except Exception:
        return False

def updateUsuario(password,permisos,id):
    try:
        con=get_db()
        cur=con.cursor()
        #sql="UPDATE persona INNER JOIN usuario ON(persona.id = usuario.id) SET persona.nombre = ?, persona.sexo = ?, persona.direccion=?, usuario.password=?, usuario.permisos=? WHERE persona.id = ?;"
        sql="UPDATE usuario SET password=?, permisos=? WHERE id=?;"
        cur.execute(sql,(password,permisos,id))
        con.commit()
        con.close()
        return True
    except Exception:
        return False


def consUsuarioPassword(usuario):
    try:
        con=get_db()
        cur=con.cursor()
        sql="select * from usuario where usuario=?"
        cur.execute(sql,(usuario,))
        user=cur.fetchall()
        con.close()
    except Exception: #Esto se ejecuta solamente cuando sale una excepcion en la busqueda, como cuando no encuentra un dato.
        return None

    return user

def eliminarUsuario(id):
    try:
        con=get_db()
        cur=con.cursor()
        #sql="UPDATE persona INNER JOIN usuario ON(persona.id = usuario.id) SET persona.nombre = ?, persona.sexo = ?, persona.direccion=?, usuario.password=?, usuario.permisos=? WHERE persona.id = ?;"
        sql="delete from usuario where id=?;"
        cur.execute(sql,(id,))
        con.commit()
        con.close()
        return True
    except Exception:
        return False

def eliminarPersona(id):
    try:
        con=get_db()
        cur=con.cursor()
        #sql="UPDATE persona INNER JOIN usuario ON(persona.id = usuario.id) SET persona.nombre = ?, persona.sexo = ?, persona.direccion=?, usuario.password=?, usuario.permisos=? WHERE persona.id = ?;"
        sql="delete from persona where id=?;"
        cur.execute(sql,(id,))
        con.commit()
        con.close()
        return True
    except Exception:
        return False