import pandas as pd
import numpy as np


columnas=input("Ingrese el numero de columnas que va a listar: ")
myInput = int(columnas)

df = pd.DataFrame({'uno': [1, 2, 3], 'dos': [4, 5, 6], 'tres': [7, 8, 9]}, index=['x', 'y', 'z'])

lista_recorrer = []


datos=pd.read_csv('DATOS_PROYECTO_SENSOR.csv',sep=',',header=0)

df=pd.DataFrame(datos, columns=['fecha','temperatura'])


df['fecha'] =  pd.to_datetime(df['fecha'])

df = df.set_index(['fecha'])




df.to_csv('AgrupacionDatos.csv', sep=',')

datos2 = pd.read_csv('AgrupacionDatos.csv',sep=',',header=0)

df3 = pd.DataFrame(datos2, columns=['temperatura'])

df3['temperatura'] = df3['temperatura'].astype(float)


df31 = pd.DataFrame(datos2, columns=['fecha'])


aux = 0

valor = 4


while aux<int(df3.count()):
    while valor >= 0:
        if (aux - valor)< 0:
            print("nan")
            lista_recorrer.append('NaN')
            valor = valor - 1
        else:
            print (df3["temperatura"][aux-valor])
            lista_recorrer.append(df3['temperatura'][aux-valor])
            valor = valor - 1
            valor = 4
            aux = aux + 1
            lista_total =[]
            total = len (lista_recorrer)
            d= {'Fecha': df31['fecha']}
            df5 = pd.DataFrame(d)
            matriz = []
            s = 0
            for i in range(int(df5.count())):
                matriz.append([])
                for j in range(valor+1):
                    matriz[i].append(float(lista_recorrer[s]))
                    s = s + 1
                    dfinal = pd.DataFrame(matriz)
                    frames = [df5, dfinal]
                    resultado = pd.concat(frames, axis=1)
                    print(resultado)
                    resultado.to_csv('Escenario1.csv', sep=',')