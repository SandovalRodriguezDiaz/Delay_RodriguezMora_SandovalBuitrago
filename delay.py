import numpy as np
import math

class DELAY():
    def __init__(self, miliS, repeticiones, arreglo):
        self.miliS=miliS
        self.repeticiones=repeticiones
        self.arreglo=arreglo

    def funcion(self):
        Narreglo=[]
        mmil=self.miliS/1000.0
        DT=int(44100*mmil)
        D=(math.e)

        for j in range(0, self.repeticiones):
            aux=[]
            k=DT*j
            for h in range(0, k):
                aux.append(0)
            for y in range(0, len(self.arreglo)):
                aux.append(self.arreglo[y][0])
            for i in range(0, len(self.arreglo)):
                b=self.arreglo[i][0]+aux[i]
                Narreglo.append(b)
            for t in range(len(self.arreglo), len(aux)):
                Narreglo.append(aux[t])

        Naudio=np.asanyarray(Narreglo)
        return Naudio