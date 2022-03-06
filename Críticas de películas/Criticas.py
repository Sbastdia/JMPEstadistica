
import numpy
import JMPEstadisticas as jmp
filename = '/home/alberto/Documentos/UAX/Curso 2/Cuatrimestre 2/Programación Paralela/Críticas de películas/pelis.csv'
raw_data = open(filename)
data = numpy.loadtxt(raw_data, delimiter=";",skiprows=1)
print(data.shape)
stats = jmp.JMPEstadisticas(data)
stats.analisisCaracteristica()