import pandas as pnd
import numpy as np
import JMPEstadisticas as jmp
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, 'datos.csv')
print("Hola")
#filename = 'datos.csv'
raw_data = open(filename)
data = np.loadtxt(raw_data, delimiter=";",skiprows=1)
data=pnd.DataFrame({'Pesos':data})
stats = jmp.JMPEstadisticas(data["Pesos"])
stats.analisisCaracteristica()


#import csv
#filename = "datos.csv"
#with open(filename) as f:
    #header= next(f)

    #for h in header:
        #print (h, end='')