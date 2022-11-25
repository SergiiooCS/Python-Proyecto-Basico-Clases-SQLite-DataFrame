#   --   SGE - T1 - HI1 - SergioCaminoSaiz
#   --   LEER FICHERO XLSX

#Pandas lo utilizo para trabajar con datos de otros ficheros.



#   --   Guardar archivo en variable.
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
'''



#   --   Crear Dataframe para el archivo.
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)
'''




#   --   Eliminar celdas NaN.
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)

#Comprobar los datos.
def comprobarDatos(df1):
    for i in range(len(df1)):
        for x in df1.loc[i].isna():
            if x:
                print(f'NaN en : {i}, {x}')
                
#Imprimir los datos comprobados. 
def imprimirDatos(df1):
    for x in range(len(df1)):
        print(df1.loc[x])

imprimirDatos(df1)
comprobarDatos(df1)
'''



#   --   Crear colecciones de datos a partir del Dataframe.
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


#Tenemos que convertir el Dataframe en una Serie para despues poder meterlo en una Lista. 
#Serie : 
serie = df1.iloc[11]

# Lista : 
lista1=serie.to_list()
print(lista1)

# Tupla : 
tupla1 = (df1.iloc[15])
print(tupla1) 



# Conjunto : 
fila3=df1.iloc[25]
conjunto1 = {fila3.to_list}
print(conjunto1) 




# Diccionario : 
def recorrer(column):
    for i in range(len(df1)):
        print(df1.iloc[i][column])
       
        
       
fila4 = print(recorrer(2020))
 
diccionario1 = {fila4}
print(diccionario1)
'''




#   --   Concatenar todos los datos de la lista y guardarlo en un fichero de texto con el nombre "lista.txt".
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)

#Tenemos que convertir el Dataframe en una Serie para despues poder meterlo en una Lista. 
res = []
for x in range(len(df1.columns)):
    res.append(df1.iloc[x])


for x in range(len(res)):
    res[x] = res[x].to_list()


archivo = "src/lista.txt"
f = open(archivo, 'a+')
for i in res:
    f.write(f" {i}, ")
f.close()
'''













#   --   Funcion que cambia las filas por columnas para tener dataframe con años. 
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)

def cambiarFilas(df1):
    dfColumnas = df1.transpose()
    print(dfColumnas)

cambiarFilas(df1)
'''








#   --   Funcion que recorra las columnas y calcule la media, varianza y la moda. 
'''
import pandas as pd
import numpy as np
from statistics import mode
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)



#Funcion media.    
def media(df1):
    filas = len(df1)
    total = 0
    for i in range(filas):
        for y in df1.iloc[i]:
            if type(y) != str:
                total+=y
                break
    print(f"Total es {total}")
    print(f"La media es {total/filas}")

    

 
#Funcion varianza.
def varianza(column):
    resultado=df1[column]
    return np.var(resultado)


#Funcion moda.
def moda(column):
    dfModa=df1[column]
    return mode(dfModa)    



print("Media:")
print(media(df1))



print("Varizanza:")
print(varianza(2019))


print("Moda:")
print(moda(2019))
'''








#   --   Utiliza un map para crear una funcion para el dataframe. 

#Necesito saber como acceder a un dato especifico (columna y fila)
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


dato1 = df1.iloc[11]
dato2 = df1.iloc[12]
dato3 = df1.iloc[13]
dato4 = df1.iloc[14]



def doble(numero):
    return numero*2


    
numeros=[dato1,dato2,dato3,dato4]
mapeo=map(doble,numeros)
resultado=list(mapeo)
print(resultado)
'''












#   --   Utilizar filter para crear una funcion que extraiga un sub-dataset.
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0',  header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


dato1 = df1.iloc[11]
dato2 = df1.iloc[12]
dato3 = df1.iloc[13]
dato4 = df1.iloc[14]


def positivo(numero):
    x=int(numero)
    if(x>0):
        resultado=print("Es mayor a 0")
        return resultado
    else:
        resultado=print("Es menor a 0")
        return resultado


    
numeros=[dato1,dato2,dato3,dato4]
filtro=filter(positivo,numeros)
resultado=list(filtro)
print(resultado)
'''









#   --   Crea una clase que tenga como atributos las columnas.
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0', header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


class Objeto:
    
    def __init__(self,df1):
        for x in range(len(df1.columns)):
            self.df1=df1.columns[x]
        
#Instanciar la clase        
prueba1 =Objeto(df1)
print(prueba1)
'''









#   --   Define una forma de imprimir los objetos de la clase en la que aparezcan todos los datos de la clase. 
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0', header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


class Objeto:
    
    def __init__(self,df1):
        for x in range(len(df1.columns)):
            self.df1=df1
            setattr(self,f"{df1.columns[x]}", float())
            
        
    def saludar(self):
        print("Objeto creado a partir de clase")
        
    def __str__(self):
            resultado = print(f" Contenido del objeto : {vars(self.df1)}")
            return resultado


prueba1 = Objeto(df1)
#objetoPrueba.__str__()
'''








#   --   Crea métodos para modificar el valor de cada atributo.
'''
import pandas as pd
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0', header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


class Objeto:
    
    def __init__(self,df1):
        for x in range(len(df1.columns)):
            self.df1=df1
            setattr(self,f"{df1.columns[x]}", float())
            
        
    def saludar(self):
        print("Objeto creado a partir de clase")
        
    def __str__(self):
            resultado = print(f" Contenido del objeto : {vars(self.df1)}")
            return resultado
            
            
    def cambiar(self, objeto, columna, parametro):
        for x in range(len(objeto.columns[columna])):
            self.objeto=parametro         
            
            
        print("Objeto cambiado")        
            
            
    

objetoPrueba = Objeto(df1)
objetoPrueba.__str__()
objetoPrueba.cambiar(df1, 5, "Hola")

'''














#   --   Crea una base de datos en SQLite desde Python. 
'''
import sqlite3 as sq
con = sq.connect("hito.db")
'''







#   --   Guarda el dataset como tabla en la base de datos
'''
import sqlite3 as sq
import pandas as pd

#Dataframe
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0', header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


#SQLite - Guardar Dataframe
con = sq.connect("hito.db")
#Esto hace que podamos guardar el dataframe dentro de la tabla (solo se debe hacer una vez).
df1.to_sql(name='hito', con=con)
select = pd.read_sql('select * from hito;', con)
'''










#   --   Realizar al menos 3 consultas distintas.
'''
import sqlite3 as sq
import pandas as pd

#Dataframe
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0', header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


#SQLite - Conectar a la BD.
con = sq.connect("hito.db")
cur = con.cursor()

#Sentencia 1 :

for row in cur.execute("SELECT * FROM hito;"):
    print(row)

#Sentencia 2 :
sentencia2 = cur.execute("INSERT INTO hito('index', '2020') VALUES('Prueba', 24534);")    
print(sentencia2.fetchone())

#Sentencia 3 :
sentencia3 = cur.execute("DELETE FROM hito WHERE 'index'='Prueba';")
'''





#   --   Guardar los datos de las consultas en un dataframe.
'''
import sqlite3 as sq
import pandas as pd

#Dataframe
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0', header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


#SQLite - Conectar a la BD.
con = sq.connect("hito.db")
cur = con.cursor()

#SENTENCIAS
#Sentencia 1 :
sentencia1 = cur.execute("SELECT * FROM hito;")    
print(sentencia1.fetchone())
dfSentencia1 = pd.DataFrame(sentencia1)
#print(dfSentencia1)


#Sentencia 2 :
sentencia2 = cur.execute("INSERT INTO hito('index', '2020') VALUES('Prueba', 24534);")    
print(sentencia2.fetchone())
dfSentencia2 = pd.DataFrame(sentencia2)
#print(dfSentencia2)

#Sentencia 3 :
sentencia3 = cur.execute("DELETE FROM hito WHERE 'index'='Prueba';")
print(sentencia3.fetchone())
dfSentencia3 = pd.DataFrame(sentencia3)
#print(dfSentencia3)
'''














#   --  Guarda el nuevo dataframe como una nueva tabla en la base de datos
'''
import sqlite3 as sq
import pandas as pd

 #Dataframe
File = pd.read_excel(r'src/datos.xlsx', sheet_name='tabla-0', header=7)
df1 = pd.DataFrame(File)
df1.fillna(0, inplace=True)


 #SQLite - Guardar Dataframe
con = sq.connect("hito.db")
cur = con.cursor()


#SENTENCIAS
#Sentencia 1 :
sentencia1 = cur.execute("SELECT * FROM hito;")    
print(sentencia1.fetchone())
dfSentencia1 = pd.DataFrame(sentencia1)


dfSentencia1.to_sql(name='hitoentencia1', con=con)
select1 = pd.read_sql('select * from hitoentencia1;', con)
print("Dataframe de sentencia 1 importado correctamente")



#print(dfSentencia1)


#Sentencia 2 :
sentencia2 = cur.execute("INSERT INTO hito('index', '2020') VALUES('Prueba4', 2000);")    
print(sentencia2.fetchone())
dfSentencia2 = pd.DataFrame(sentencia2)
#print(dfSentencia2)

dfSentencia2.to_sql(name='hitoentencia2', con=con)
select2 = pd.read_sql('select * from hitoentencia2;', con)
print("Dataframe de sentencia 1 importado correctamente")




#Sentencia 3 :
sentencia3 = cur.execute("DELETE FROM hito WHERE 'index'='Prueba';")
print(sentencia3.fetchone())
dfSentencia3 = pd.DataFrame(sentencia3)
#print(dfSentencia3)



dfSentencia3.to_sql(name='hitoentencia3', con=con)
select3 = pd.read_sql('select * from hitoentencia3;', con)
print("Dataframe de sentencia 1 importado correctamente")



#CERRAR CONEXION
con.close()
print("CONEXION CERRADA")
'''