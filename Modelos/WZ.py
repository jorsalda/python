#!/usr/bin/env python
#-*- coding: utf-8 -*
from scipy.stats import norm
from scipy.stats import t
import math
from Tkinter import *
z=0.0
a=0.0

def fwzz():
    ventana = Tk()
    ventana.geometry("800x800+800+200")
    ventana.config(bg="orange2")
    def fwz():
    
        global z
        al=v2.get()
        val=(al/100.0)+(((1-(al/100.0))))/2
        z=norm.ppf(val)
        #varres.set("z acumuladao="+str(round(z,3)))
        Label(ventana, text="Nivel de confianza", fg="black").place(x=10, y=120)
        Label(ventana, text=al, fg="red").place(x=130, y=120)
        Label(ventana, text="%", fg="black").place(x=160, y=120)
        Label(ventana, text="Z-Acumulada:", fg="black").place(x=10, y=140)
        Label(ventana, text=round(val,3), fg="red").place(x=105, y=140)
        Label(ventana, text="Z-Estimado", fg="black").place(x=10, y=160)
        Label(ventana, text=round(z,2), fg="red").place(x=105, y=160)
        print "al=",al
        #ventana.create_text(text="Intervalo de Confianza para la estimacion puntual",fill='black',font=('verdena', 10, 'bold'))      
        return z
    
    """data = IntVar()

    entry = Entry(textvariable=data)"""
    
    v2=IntVar(ventana,value=0)
    Entry(ventana,textvariable=v2,bg="black", fg="red").place(x=100,y=25)
    #Entry(textvariable=v3,bg="black", fg="red").place(x=20, y=120)
    #txt1=Entry(ventana,textvariable=vartxt1).place(x=10,y=0)
    bsum=Button(ventana,command=fwz,text='Gauss::Z',padx=42,pady=5).place(x=100, y=50)
    #blim=Button(ventana,command=limpiar,text='limpiar',padx=42,pady=5).place(x=0,y=170)
    
    ventana.mainloop()
    


#fwzz()