from os import error
import sqlite3
from sqlite3 import Error
import os
import time

CURR_DIR = os.getcwd() #Obtiene el directorio actual madre

URL_DB=CURR_DIR+"\proyectoUsuarios\database.db"

def get_db():
    try:
        con = sqlite3.connect(URL_DB)
        return con
    except :
        print ('error')

'''
try:
    #strsql = "select * from registro where id='"+"123"+"' or usuario='"+"car"+"';"# and correo="+correo+";"
    strsql = "select * from persona"
    con = get_db()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    persona = cursorObj.fetchall() #Obtenemos la información de la consulta
    #print(persona)
    if(len(persona)>0):
        con.close()
        print(True)
    else:
        con.close()
        print(False)
except Error as err:
    print(err)
    con.close()'''

from db.db import insertPersona,insertUsuario,consID,consUsuario

'''
def insertPersona(id,nombre,sexo,direccion):
    con1=get_db()
    cur1=con1.cursor()
    sqlInsert_persona="INSERT INTO persona(id, nombre, sexo, direccion) VALUEs (?, ?, ?, ?);"
    cur1.execute(sqlInsert_persona,(id,nombre,sexo,direccion))
    con1.commit()
    con1.close()

def insertUsuario(id,usuario,password,permisos):
    con1=get_db()
    cur1=con1.cursor()
    sqlInsert_usuario="INSERT INTO usuario(id, usuario, password, permisos) VALUEs (?, ?, ?, ?);"
    cur1.execute(sqlInsert_usuario,(id,usuario,password,permisos))
    con1.commit()
    con1.close()

def consID(id):
    con=get_db()
    cur=con.cursor()
    sql_consulta_persona="select * from persona where id=?;"
    res_persona=cur.execute(sql_consulta_persona,(id,)) #Si es solo un dato se debe agregar una coma
    persona = cur.fetchall()
    return len(persona)

def consUsuario(usuario):
    con=get_db()
    cur=con.cursor()
    sql_consulta_usuario="select * from usuario where usuario=?"
    res_usuario = cur.execute(sql_consulta_usuario,(usuario,))
    user=cur.fetchall()
    return len(user)
'''
nombre="Juanpis"
id="123445"
sexo="M"
direccion="Cll 123"
usuario="juanpis11"
password="123456"
permisos="usuario"

persona=consID(id)

if(persona>0):
    print("Cedula ya registrada")
else:
    user=consUsuario(usuario)

    if(user>0):
        print("Usuario ya registrado")
    
    else:
        insertPersona(id,nombre,sexo,direccion)
        insertUsuario(id,usuario,password,permisos)
        print("Puede registrar el usuario")




'''
nombre="Juanpis"
id=1234
sexo="M"
direccion="Cll 123"
usuario="juanpis1"
password="123456"
permisos="usuario"

sqlInsert_usuario="INSERT INTO usuario(id, usuario, password, permisos) VALUEs (?, ?, ?, ?)"
con=get_db()
cur=con.cursor()
cur.execute(sqlInsert_usuario,(id,usuario,password,permisos))
con.commit()
'''