from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
import struct
import tkMessageBox
from reproductro import reproductor
from cuadros import funcion
from Archivar import file
from delay import DELAY
import matplotlib.pylab as plt
import wave


def main():
    ventana=Tk()

    ventana.title("Generador de Filtro / Delay")

    frame1 = Frame(ventana)
    frame1.pack(side=TOP)
    frame2 = Frame(ventana)
    frame2.pack(side=TOP)
    frame3 = Frame(ventana)
    frame3.pack(side=TOP)
    frame4 = Frame(ventana)
    frame4.pack(side=TOP)
    frame5=Frame(ventana)
    frame5.pack(side=TOP)
    frame6=Frame(ventana)
    frame6.pack(side=TOP)
    frame7=Frame(ventana)
    frame7.pack(side=TOP)
    frame8=Frame(ventana)
    frame8.pack(side=TOP)
    frame9 = Frame(ventana)
    frame9.pack(side=TOP)
    frame10 = Frame(ventana)
    frame10.pack(side=TOP)
    frame11 = Frame(ventana)
    frame11.pack(side=TOP)
    frame12 = Frame(ventana)
    frame12.pack(side=TOP)
    frame13=Frame(ventana)
    frame13.pack(side=TOP)
    frame14=Frame(ventana)
    frame14.pack(side=TOP)
    frame15=Frame(ventana)
    frame15.pack(side=TOP)

    global frames, audiofile
    frames=0
    audiofile=[]

    def pi():
        global frames

        if selc.get() == 1:

            frames=int(44100*(1/float(frecuencia.get())/2.0))

        if selc.get() == 2:

            frames=int(44100*(1/float(frecuencia.get())/4.0))

        if selc.get() == 3:

            frames=int(44100*(1/float(frecuencia.get())/8.0))

        if selc.get() == 4:

            frames=int(44100*(1/float(frecuencia.get())/16.0))


    def generar():

        global frames

        Dur=int(duracion.get())
        ton=int(frecuencia.get())
        vol=Volumen.get()

        if selc.get() !=0:
            a=funcion(Dur,ton,frames)
            arreglo=a.crear()
            ajuste=a.niveldeaudio(vol,arreglo)
            doc=file(44100,16,Nombre.get())
            doc.archive(ajuste)
            print (frames)

        else:
            frames=int(cuadros.get())
            a=funcion(Dur,ton,frames)
            arreglo=a.crear()
            ajuste=a.niveldeaudio(vol,arreglo)
            doc=file(44100,16,Nombre.get())
            doc.archive(ajuste)
            print (frames)

        sonido=reproductor(1024)
        Datos=sonido.open(Nombre.get())
        sonido.start(Datos[0],Datos[1],Datos[2])
        sonido.play(Datos[3])
        sonido.closed()

        plt.plot(ajuste, color="green", linewidth=1.0, linestyle="-")
        plt.show()

    def abrir():

        global audiofile

        direccion= askopenfilename()

        archivo=wave.open(direccion, "rb")
        arreglo=int(archivo.getnframes())

        for i in range(0, arreglo):
            datos=archivo.readframes(1)
            packed_value = struct.unpack('<h', datos)
            audiofile.append(packed_value)


    def generardelay():
        global audiofile
        rep=int(repetir.get())
        milis=int(milisegundos.get())
        a=DELAY(milis, rep, audiofile)

        delayarreglo=a.funcion()

        doc=file(44100,16,NombreD.get())
        doc.archive(delayarreglo)

        sonido=reproductor(1024)
        Datos=sonido.open(NombreD.get())
        sonido.start(Datos[0],Datos[1],Datos[2])
        sonido.play(Datos[3])
        sonido.closed()





    mensaje1 = Label(frame1, fg='red', padx=15, pady=10, text='Generador de Filtro')
    mensaje1.pack(side=LEFT)

    name= Label(frame2, fg="black", padx=15, pady=10, text="Ingrese el nombre del archivo nuevo:")
    name.pack(side=LEFT)

    Nombre = Entry(frame2, bd=5, insertwidth=1)
    Nombre.pack(side=LEFT, padx=15, pady=10)

    onda= Label(frame3, fg="black", padx=15, pady=10, text="Ingrese el tono a generar:                     ")
    onda.pack(side=LEFT)

    frecuencia=Entry(frame3, bd=5, insertwidth=1)
    frecuencia.pack(side=LEFT, padx=15, pady=10)

    tiempo= Label(frame4, fg="black", padx=15, pady=10, text="Ingrese la duracion:                                ")
    tiempo.pack(side=LEFT)

    duracion=Entry(frame4, bd=5, insertwidth=1)
    duracion.pack(side=LEFT, padx=15, pady=10)

    cuadro= Label(frame5, fg="black", padx=15, pady=10, text="Ingrese los cuadros que desea retrazar\nla onda:")
    cuadro.pack(side=LEFT)

    cuadros=Entry(frame5, bd=5, insertwidth=1)
    cuadros.pack(side=LEFT, padx=15, pady=10)

    selc=IntVar()

    Pi=Radiobutton(frame6,text='pi',value=1,variable=selc, command=pi)
    Pi.pack(side=LEFT)

    Pi2=Radiobutton(frame6,text='pi/2',value=2,variable=selc, command=pi)
    Pi2.pack(side=LEFT)

    Pi4=Radiobutton(frame6,text='pi/4',value=3,variable=selc, command=pi)
    Pi4.pack(side=LEFT)

    Pi8=Radiobutton(frame6,text='pi/8',value=4,variable=selc, command=pi)
    Pi8.pack(side=LEFT)

    Volumen= Scale(frame7, label='Volumen', orient=HORIZONTAL,width=10, length=250,from_=-1,to=-20)
    Volumen.pack(side=TOP, padx=1,pady=1)

    Reproducir=Button(frame8,padx=30, pady=2,text="Reproducir y Graficar",command=generar)
    Reproducir.pack(side=LEFT)

    mensaje2 = Label(frame9, fg='red', padx=15, pady=10, text='Delay')
    mensaje2.pack(side=LEFT)

    nameD= Label(frame10, fg="black", padx=15, pady=10, text="Ingrese el nombre del archivo nuevo:")
    nameD.pack(side=LEFT)

    NombreD = Entry(frame10, bd=5, insertwidth=1)
    NombreD.pack(side=LEFT, padx=15, pady=10)

    Archivo=Button(frame11, padx=30, pady=2,text="Cargar archivo",command=abrir)
    Archivo.pack(side=LEFT)

    repeticiones= Label(frame12, fg="black", padx=15, pady=10, text="Ingrese numero de repeticiones          ")
    repeticiones.pack(side=LEFT)

    repetir = Entry(frame12, bd=5, insertwidth=1)
    repetir.pack(side=LEFT, padx=15, pady=10)

    ms= Label(frame13, fg="black", padx=15, pady=10, text="Ingrese los milisegundos                      ")
    ms.pack(side=LEFT)

    milisegundos = Entry(frame13, bd=5, insertwidth=1)
    milisegundos.pack(side=LEFT, padx=15, pady=10)


    ReproducirD=Button(frame15,padx=30, pady=2,text="Reproducir",command=generardelay)
    ReproducirD.pack(side=LEFT)


    ventana.mainloop()




if __name__=="__main__":
    main()