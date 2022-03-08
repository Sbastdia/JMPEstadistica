from collections import Counter
from math import *
import matplotlib.pyplot as plt
from scipy.stats import norm



class JMPEstadisticas:

    def __init__(self,caracteristica):
        self.caracteristica = caracteristica

    def calculoMediaAritmetica(self):

        n = self.caracteristica.count()
        sumaValoresObservaciones = 0
        mediaAritmetica = 0
        for valorObservacion in self.caracteristica:
            sumaValoresObservaciones += valorObservacion

        mediaAritmetica = sumaValoresObservaciones / n
        return mediaAritmetica

    def calculoVarianzaDesviacionTipica(self):
        n = self.caracteristica.count()
        mediaAritmetica = self.caracteristica.mean()
        varianza = 0
        c3 = 0
        for valorObservacion in self.caracteristica:
            c1 = valorObservacion - mediaAritmetica
            c2 = c1 * c1
            c3 += c2

        varianza = c3 / (n - 1)

        desviacionTipica = sqrt(varianza)

        return ([varianza, desviacionTipica])
    def Calculos(self,peso):
        n=peso-self.calculoMediaAritmetica()
        valor=n/ self.calculoVarianzaDesviacionTipica()[1]

    def calculo (self, peso):
        valor=norm.cdf(peso, self.calculoMediaAritmetica(), self.calculoVarianzaDesviacionTipica()[1])
        print(valor)
    #def visualizacion(self):
        #Grafica distribucion normal y linea de donde nos lo ha pedido


    def analisisCaracteristica(self):

        print("-----------------------------------------")
        print("      MEDIDA DE TENDENCIA CENTRAL        ")
        print("-----------------------------------------\n")

        print("-- CANTIDAD DE OBSERVACIONES --")
        # -Cantidad de observaciones
        n = self.caracteristica.count()
        print("Cantidad de observaciones = " + str(n))

        # -Media artimética:
        print("\n-- MEDIA --")
        media = self.calculoMediaAritmetica()
        print("Peso medio = " + str(media))
        print("> Observaciones: Si todas las observaciones tuvieran el mismo valor (reparto equitativo), este sería " + str(media))


        print("\n\n-----------------------------------------")
        print("      MEDIDA DE DISPERSION        ")
        print("-----------------------------------------\n")

        varianzaDesviacionTipica = self.calculoVarianzaDesviacionTipica()

        print("\n-- DESVIACION TIPICA --")
        print("Desviación típica calculada = " + str(varianzaDesviacionTipica[1]))


        print("\n-- PROBABILIDADES --")
        print("Introduzca el número para calcular la probabilidad de que una naranja escogida al azar pese menos que ese número")
        peso=input()
        print(f"Vamos a calcular la probabilidad de que una naranja pese menos que {peso}")
        self.calculo(peso)
        #self.visualizacion()