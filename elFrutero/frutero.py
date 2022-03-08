import pandas as pnd
import numpy as np
import JMPEstadisticas as jmp
print("Hola")
filename = '/home/alberto/Documentos/UAX/Curso 2/Cuatrimestre 2/Programación Paralela/JMPEstadistica/elFrutero/datos.csv'
raw_data = open(filename)
data = np.loadtxt(raw_data, delimiter=";",skiprows=1)
data=pnd.DataFrame({'Pesos':data})
stats = jmp.JMPEstadisticas(data["Pesos"])
stats.analisisCaracteristica()
