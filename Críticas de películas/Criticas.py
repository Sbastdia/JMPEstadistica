
import numpy
import JMPEstadisticas as jmp
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, 'pelis.csv')
raw_data = open(filename)
data = numpy.loadtxt(raw_data, delimiter=";",skiprows=1)
print(data.shape)
stats = jmp.JMPEstadisticas(data)
stats.analisisCaracteristica()