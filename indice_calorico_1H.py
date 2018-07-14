import pandas as pd

#Declaro Matriz 
Array = []
#Leo el archivo csv
data=pd.read_csv('Data_Sensor.csv',sep=',',header=0)
DF=pd.DataFrame(data, columns=['fecha','indice_calorico'])
#convierto tipo de dato
DF['fecha'] =  pd.to_datetime(DF['fecha'])
DF = DF.set_index(['fecha'])
DF2 = DF.resample('300S').mean()
#borro valores en nulo
DF2 = DF2.dropna()
print (DF2)
DF2.to_csv('AgrupacionDatos.csv', sep=',')
data2 = pd.read_csv('AgrupacionDatos.csv', sep=',',header=0)

DF3 = pd.DataFrame(data2, columns=['indice_calorico'])
DF3['indice_calorico'] = DF3['indice_calorico'].astype(float)

DF31 = pd.DataFrame(data2, columns=['fecha'])
#Cuantas horas atras
aux = 0
valor = 4
#recorro la matriz 
while (aux < int(DF3.count())):
    while (valor >= 0):
        if ((aux - valor)< 0):
            #print ('NaN')
            Array.append('NaN')
            valor = valor - 1
        else:
            #print (DF3['indice_calorico'][aux-valor])
            Array.append(DF3['indice_calorico'][aux-valor])
            valor = valor - 1
    valor = 4
    aux = aux + 1

    
lista_total =[]

total = len (Array)

d= {'Fecha': DF31['fecha']}
DF5 = pd.DataFrame(d)

matriz = []
s = 0
for i in range(int(DF5.count())):
    matriz.append([])
    for j in range(valor+1):          
        matriz[i].append(float(Array[s]))
        s = s + 1


DFinal = pd.DataFrame(matriz)
frames = [DF5, DFinal]
resultado = pd.concat(frames, axis=1)
#Elimino valores con NaN
resultado = resultado.dropna()
print(resultado)
resultado.to_csv('Escenario1.csv', sep=',')