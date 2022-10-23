from IPython.core.interactiveshell import InteractiveShell # Nos permite mostar más de una salida por celda
InteractiveShell.ast_node_interactivity = "all" # Nos permite mostar más de una salida por celda

import pandas as pd
import numpy as np
import mysql.connector
pd.options.display.max_columns=None
class Crear_bbdd_tablas:
    
    
    def __init__(self, nombre_bbdd):
        self.nombre_bdd= nombre_bbdd
        
        
    
    def crear_bbdd(self,nombre_bbdd):

        mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password='AlumnaAdalab'
        )
        print("Conexión realizada con éxito")
        
        mycursor = mydb.cursor()

        try:
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bbdd};")
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)



    def crear_insertar_tabla(self,nombre_bbdd, query):
    
        # nos conectamsos con el servidor usando el conector de sql
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                                        host='127.0.0.1', database=f"{nombre_bbdd}")
        # iniciamos el cursor
        mycursor = cnx.cursor()
        
        # intentamos hacer la query
        try: 
            mycursor.execute(query)
            cnx.commit() 
        # en caso de que podamos ejecutar la query devuelvenos un error para saber en que nos estamos equivocando
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
        