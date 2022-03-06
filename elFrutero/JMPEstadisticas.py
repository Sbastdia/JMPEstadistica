from collections import Counter
from math import *
import matplotlib.pyplot as plt



class JMPEstadisticas:

    def __init__(self,caracteristica):
        self.caracteristica = caracteristica

    def CalculoMedia(self):
        sumaProducto=0
        sumaFrecuencia=0
        for elemento in self.caracteristica:
            producto=elemento[0]*elemento[1]
            frecuencia=elemento[1]
            sumaProducto+=producto
            sumaFrecuencia+=frecuencia
        media=sumaProducto/sumaFrecuencia
        media=round(media,2)
        return media

    def CalculoVarianza(self):
        Sumavarianza=0
        sumaFrecuencia=0
        media=self.CalculoMedia()
        for elemento in self.caracteristica:
            varianza=elemento[1]*pow((int(elemento[0])-media),2)
            frecuencia=elemento[1]
            sumaFrecuencia+=frecuencia
            Sumavarianza+=varianza
        Varianza=Sumavarianza/sumaFrecuencia
        desviacionTipica = sqrt(Varianza)

        return ([Varianza, desviacionTipica])
    def vis(self):
        notas=[]
        frecuencia=[]
        for elemento in self.caracteristica:
            notas.append(elemento[0])
            frecuencia.append(elemento[1])
        plt.bar(notas,frecuencia,0.3)
        #plt.hist(self.caracteristica)
        plt.title("Opiniones obtenidas para una película")
        plt.plot(notas,frecuencia,marker='o', color='#ff8200')
        plt.show()

    def visualizacion(self,media,mediana,cuartil_1,cuartil_2,cuartil_3):

        plt.subplot(2, 2, 1)
        plt.hist(self.caracteristica)
        plt.title("Histograma y media")
        plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 2)
        plt.hist(self.caracteristica)
        plt.title("Histograma y mediana")
        plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1,label = str(mediana))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 3)
        plt.hist(self.caracteristica)
        plt.title("Histograma y cuartiles")
        plt.axvline(cuartil_1, color='orange', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil_1))
        plt.axvline(cuartil_2, color='orange', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil_2))
        plt.axvline(cuartil_3, color='orange', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil_3))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 4)
        plt.boxplot(self.caracteristica)
        plt.title("Diagrama de caja y bigotes")
        plt.show()

    def cantidadObs(self):
        cantidad=0
        for elemento in self.caracteristica:
            cantidad+=elemento[1]
        return cantidad

    def OrdenarF(self):
        orden=sorted(self.caracteristica, key=lambda e: e[1])
        return orden

    def OrdenarN(self):
        orden=sorted(self.caracteristica, key=lambda e: e[0])
        return orden

    def Min(self):
        orden=self.OrdenarF()
        minimo=[]
        for elemento in orden:
            if elemento[1]==orden[0][1]:
                minimo.append(elemento)
        for numero in minimo:
            print("Valor mínimo: "+ str(numero[0]) + " Frequencia: " + str(numero[1]))

    def Max(self):
        orden=self.OrdenarF()
        maximo=[]
        for elemento in orden:
            if elemento[1]==orden[-1][1]:
                maximo.append(elemento)
        for numero in maximo:
            print("Valor máximo: "+ str(numero[0]) + " Frequencia: " + str(numero[1]))
    def analisisCaracteristica(self):

        print("-----------------------------------------")
        print("      MEDIDA DE TENDENCIA CENTRAL        ")
        print("-----------------------------------------\n")

        print("-- CANTIDAD DE OBSERVACIONES --")
        # -Cantidad de observaciones
        n = int(self.cantidadObs())
        print("Cantidad de observaciones = " + str(n))
        orden=self.OrdenarF()
        print ("\n-- MIN --")
        self.Min()
        print()
        print ("\n-- MAX --")
        self.Max()


        # -Media artimética:
        print("\n-- MEDIA --")
        media = self.CalculoMedia()
        print("Media aritmética calculada = " + str(media))
        print("> Observaciones: Si todas las observaciones tuvieran el mismo valor (reparto equitativo), este sería " + str(media))


        print("\n\n-----------------------------------------")
        print("      MEDIDA DE DISPERSION        ")
        print("-----------------------------------------\n")
        print("-- RANGO --")
        print ("Rango de la serie = "+str(orden[-1][1]-orden[0][1]))
        varianzaDesviacionTipica = self.CalculoVarianza()

        print("\n-- VARIANZA --")
        print("Varianza calculada = " + str(varianzaDesviacionTipica[0]))

        print("\n-- DESVIACION TIPICA --")
        print("Desviación típica calculada = " + str(varianzaDesviacionTipica[1]))
        desviacionTipica = varianzaDesviacionTipica[1]
        print("68 % de los valores de las observaciones se sitúan entre " + str(media - desviacionTipica) + " y " + str(
            media + desviacionTipica))
        print("95 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 2)) + " y " + str(
            media + (desviacionTipica * 2)))
        print("99,7 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 3)) + " y " + str(
            media + (desviacionTipica * 3)))
        self.vis()