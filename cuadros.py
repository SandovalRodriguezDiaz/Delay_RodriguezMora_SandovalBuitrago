import numpy as np
import math


class funcion:

    def __init__(self, tiempo, tono, cuadros):

        self.tiempo=tiempo
        self.tono=tono
        self.cuadros=cuadros

    def crear(self):
        array=[]
        array2=[]
        alteracion=[]

        for i in range(0,(44100*self.tiempo)):
            valores=math.sin((2*math.pi*self.tono*i)/44100.0)
            array.append(valores)
        for i in range (0,self.cuadros):
            array2.append(0)
        for i in range(0,(len(array)-self.cuadros)):
            array2.append(array[i])
        for i in range(0,len(array)):
            a=array[i]+array2[i]
            alteracion.append(a)

        Naudio=np.asanyarray(alteracion)

        return Naudio

    def niveldeaudio(self, nivel, info):
        VaP=max(abs(info))
        valornivel=(10**(nivel/20.0))*((2**16)/2)
        valorajustado=valornivel/float(VaP)
        infoajustada=info*valorajustado
        return infoajustada



