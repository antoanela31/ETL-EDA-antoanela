from IPython.core.interactiveshell import InteractiveShell # Nos permite mostar más de una salida por celda
InteractiveShell.ast_node_interactivity = "all" # Nos permite mostar más de una salida por celda

import requests
import pandas as pd
import numpy as np
import pandas as pd
import mysql.connector
pd.options.display.max_columns=None

#cargamos el df del que se extraerán los datos para cargarlos en sql

df= pd.read_csv('C:\Users\antoa\Desktop\ADALAB\reevaluacion\reevaluacion-modulo2-da-promo-b-nombre_antoanela\df_eda_limpieza.csv')


print("csv cargado")


# creamos el imput para solicitarle al usuario los datos para la extraccion del país que deseen

nombre_bbdd = input("Indica el nombre de tu base de datos a crear ")
print("---------------------------------------------------------------")


import Crear_bbdd_tablas as ant #importamos nuestra libreria

# iniciamos la clase
mydb = ant.crear_bbdd(nombre_bbdd)


print(f"Estamos creando tu base de datos {nombre_bbdd}")


print("-----------------------------------------")
print("base de datos formada")



# el siguiente paso es crear alguna tabla
tabla_peliculas = '''
CREATE TABLE IF NOT EXISTS `imdb`.`peliculas` (`id_pelicula` INT NOT NULL AUTO_INCREMENT, 
  `movie_title` VARCHAR(200),
  `duration` DOUBLE,
  `title_year` FLOAT, 
  `language` VARCHAR(200), 
  `country` VARCHAR (200),
  `gross` DOUBLE,
  `budget` DOUBLE, 
  `imdb_score` FLOAT, 
  `genre_1` VARCHAR(200),
  PRIMARY KEY (`id_pelicula`))
  ENGINE = InnoDB;
'''

tabla_casting = '''
CREATE TABLE IF NOT EXISTS `imdb`.`casting` (
  `id_casting` INT NOT NULL AUTO_INCREMENT,
`id_pelicula` INT NOT NULL,
 `director_name` VARCHAR (200), 
 `actor_1_name` VARCHAR (200),
`actor_2_name` VARCHAR(200), 
`actor_3_name` VARCHAR(200),
  PRIMARY KEY (`id_casting`),
  CONSTRAINT `fk_tabla_casting_peliculas`
  FOREIGN KEY (`id_pelicula`)
  REFERENCES `imdb`.`peliculas`(`id_pelicula`))
ENGINE = InnoDB;
'''

query_creacion_tabla = input("Si deseas crear una tabla, ingresa la query necesaria.Elige entre tabla_peliculas o tabla_casting")
print("---------------------------------------------------------------")
ant.crear_insertar_tabla(nombre_bbdd, query_creacion_tabla)
print("---------------------------------------------------------------")


print("El proceso ha finalizado")