#!/usr/bin/env python
#-*- coding: utf-8 -*
import os
import Pmw
import tkFont
import Tkinter
from numpy import *
from Tkinter import *
import Tkinter as tk
import numpy as np
from StringIO import StringIO
import matplotlib.pyplot as grafico
import tkFileDialog
from Archivo import*
from RLS1 import*
from INTCONFI import*
from RegLinSimp1 import*
from RLM1 import*
from RegLinMul1 import*



m=0;n=0;data=0;vy=0;vx=0;a=0;b=0

v0=Tk()
Label(v0, text="InterPronósticos S.A.S",bg="DodgerBlue3", fg="white",font=('Verdana', 32, 'bold')).place(x=10, y=240)
Label(v0, text="Los pornósticos de hoy, son la empresa del mañana",bg="DodgerBlue3", fg="orange2",font=('Verdana', 10, 'bold')).place(x=70, y=310)
Label(v0, text="Copyright::2016",bg="DodgerBlue3", fg="black",font=('Verdana', 6, 'bold')).place(x=480, y=600)
Label(v0, text="by-Jfour",bg="DodgerBlue3", fg="black",font=('Verdana', 6, 'bold')).place(x=480, y=612)

img = PhotoImage(file="logo-symbol.gif")
can = Canvas(v0, width=800, height=800)
can_width=500
can_height=80
can.pack(fill=Y,side=RIGHT,anchor=E)
can.create_image(200, 200, image=img, anchor=NW)

def leeArc(self):
    global n,m,data
    m,n,data=leerArchivo()
    return m,n,data


def ventana(m):
    global vy
    global vx
    vy=array(m[0:1])
    vx=array(m[1:2])
    grafico.scatter(vx, vy)

    grafico.show()
    return


def imprimi(m):
    global vy
    global vx
    vy=array(m[0:1])
    vx=array(m[1:2])
    y=vy.sum()
    x=vx.sum()
    Label(v0, text="Vector 1=",bg="black", fg="red").place(x=40, y=140)
    Label(v0, text=x,bg="black", fg="red").place(x=100, y=140)
    Label(v0, text="Vector 2=",bg="black", fg="red").place(x=40, y=160)
    Label(v0, text=y,bg="black", fg="red").place(x=100, y=160)
    return vy,vx

def ModRLS(m,n):
    a,b= modeloRLS(m,n)
    Label(v0, text="Modelo:",bg="black", fg="blue").place(x=50, y=180)
    Label(v0, text="Y=",bg="black", fg="red").place(x=120, y=180)
    Label(v0, text=(round(a,2)),bg="black", fg="red").place(x=150, y=180)
    Label(v0, text="+",bg="black", fg="red").place(x=190, y=180)
    Label(v0, text=(round(b,2)),bg="black", fg="red").place(x=210, y=180)
    Label(v0, text="x",bg="black", fg="red").place(x=250, y=180)

def Anova(m,n):
    SST,SSE,SSR,MSE,S2,Fc= fAnova(m,n)
    Label(v0, text="Anova:",bg="black", fg="blue").place(x=280, y=200)
    Label(v0, text="Fuente",bg="black", fg="red").place(x=60, y=220)
    Label(v0, text="df:",bg="black", fg="blue").place(x=150, y=220)
    Label(v0, text="ss:",bg="black", fg="blue").place(x=210, y=220)
    Label(v0, text="MS:",bg="black", fg="blue").place(x=305, y=220)
    Label(v0, text="fc:",bg="black", fg="blue").place(x=380, y=220)
    Label(v0, text="-----------------------------------------------------------------------",bg="black", fg="white").place(x=140, y=235)
    Label(v0, text="Regresión",bg="black", fg="red").place(x=60, y=255)
    Label(v0, text=round(SSR,2),bg="black", fg="white").place(x=210, y=255)
    Label(v0, text="Residual",bg="black", fg="red").place(x=60, y=280)
    Label(v0, text=round(SSE,2),bg="black", fg="white").place(x=210, y=280)
    Label(v0, text=round(MSE,2),bg="black", fg="white").place(x=305, y=255)
    Label(v0, text=round(S2,2),bg="black", fg="white").place(x=305, y=275)
    Label(v0, text=round(Fc,2),bg="black", fg="white").place(x=380, y=255)

    Label(v0, text="total-Corr",bg="black", fg="red").place(x=60, y=300)
    Label(v0, text=round(SST,2),bg="black", fg="white").place(x=210, y=300)
    Label(v0, text= 1,bg="black", fg="white").place(x=160, y=255)
    Label(v0, text=(n-2),bg="black", fg="white").place(x=160, y=280)
    Label(v0, text=(n-1),bg="black", fg="white").place(x=160, y=300)
    Label(v0, text=(SST/(n-1)),bg="black", fg="white").place(x=305, y=300)



def SCuadrados():
    sxx,syy,sxy= fScuad(m,n)
    r=fr(m,n)
    Label(v0, text="SUMDA CUDRADOS:",bg="black", fg="blue").place(x=180, y=320)
    Label(v0, text="Sxx",bg="black", fg="red").place(x=60, y=340)
    Label(v0, text="Syy",bg="black", fg="red").place(x=200, y=340)
    Label(v0, text="Sxy",bg="black", fg="red").place(x=340, y=340)
    Label(v0, text="C-correlacion:"r"",bg="black", fg="red").place(x=400, y=340)
    Label(v0, text=round(sxx,2),bg="black", fg="red").place(x=60, y=360)
    Label(v0, text=round(syy,2),bg="black", fg="red").place(x=200, y=360)
    Label(v0, text=round(sxy,2),bg="black", fg="red").place(x=340, y=360)
    Label(v0, text=round(r,2),bg="black", fg="red").place(x=400, y=360)


def RLS(m,n):#Regresion lienal simple
    fRegLinSimp(m,n)
def RLM(m,n,data):#Regresion Lienal Multiple
    fRegLinMulti(m,n,data)
def InterConfi(m,n):#Intervalos de confinaza
    print "endn"

def PMS(m,n):#promedio movil simple
    fInterConfi(m,n)

def finterComfiG(m,n):
        vex,vexa,vexaa,vey,veyz,veyzz=fIntConfG(m,n)

def imprimir(data):

    svy, vyct, svyc,=vectory(m)
    vy,vyt=fvy(m)
    svxc,svx,vxct=vectorx(m)
    vx,vxt=fvx(m)
    svxy,vxyt=vectorxy(m)
    fm=Frame()
    Button(fm,  text='   y    ', bg= 'black',fg= 'red').pack(side=TOP, anchor=NW)
    T = Text(fm, height=5, width=8)
    T.config(bg="black",fg="red")
    T.pack(side=TOP, anchor=NW)
    T.insert(INSERT,"","\n",vyt,"\n")
    T1 = Text(fm, height=1, width=8)
    T1.config(bg="black",fg="blue")
    T1.pack(side=TOP, anchor=NW)
    T1.insert(INSERT,"","\n",svy,"\n")
    fm.pack(side=LEFT,anchor=NW)
    fm2 = Frame()
    Button(fm2, text='  x     ', bg= 'black',fg= 'red').pack(side=TOP,anchor=SW )
    T = Text(fm2, height=5, width=8)
    T.config(bg="black",fg="red")
    T.pack(side=TOP, anchor=NW)
    T.insert(INSERT,"","\n", vxt,"\n")
    T2 = Text(fm2, height=1, width=8)
    T2.config(bg="black",fg="red")
    T2.pack(side=TOP, anchor=NW)
    T2.insert(INSERT,"","\n",svx,"\n")
    fm2.pack(side=LEFT,anchor=NW)

    fm3 = Frame()
    Button(fm3, text='   y^2    ', bg= 'black',fg= 'red').pack(side=TOP,anchor=SW )
    T = Text(fm3, height=5, width=11)
    T.config(bg="black",fg="red")
    T.pack(side=TOP, anchor=NW)
    T.insert(INSERT,"","\n", vyct,"\n")
    T3 = Text(fm3, height=1, width=11)
    T3.config(bg="black",fg="red")
    T3.pack(side=TOP, anchor=NW)
    T3.insert(INSERT,"","\n",svyc,"\n")
    fm3.pack(side=LEFT,anchor=NW)


    fm4 = Frame()
    Button(fm4, text='   x^2     ', bg= 'black',fg= 'red').pack(side=TOP,anchor=SW )
    T = Text(fm4, height=5, width=11)
    T.config(bg="black",fg="red")
    T.pack(side=TOP, anchor=NW)
    T.insert(INSERT,"","\n", vxct,"\n")
    T4 = Text(fm4, height=1, width=11)
    T4.config(bg="black",fg="red")
    T4.pack(side=TOP, anchor=NW)
    T4.insert(INSERT,"","\n", round(svxc,2),"\n")
    fm4.pack(side=LEFT,anchor=NW)


    fm5 = Frame()
    Button(fm5, text='   x*y      ', bg= 'black',fg= 'red').pack(side=TOP,anchor=SW )
    T = Text(fm5, height=5, width=11)
    T.config(bg="black",fg="red")
    T.pack(side=TOP, anchor=NW)
    T.insert(INSERT,"","\n", vxyt,"\n")
    T5 = Text(fm5, height=1, width=11)
    T5.config(bg="black",fg="red")
    T5.pack(side=TOP, anchor=NW)
    T5.insert(INSERT,"","\n", svxy,"\n")
    fm5.pack(side=LEFT,anchor=NW)

    fm6 = Frame()
    Button(fm6, text='   ý         ', bg= 'black',fg= 'red').pack(side=TOP,anchor=SW )
    T = Text(fm6, height=5, width=11)
    T.config(bg="black",fg="red")
    T.pack(side=TOP, anchor=NW)
    #T.insert(INSERT,"","\n", ys,"\n")
    T6 = Text(fm6, height=1, width=11)
    T6.config(bg="black",fg="red")
    T6.pack(side=TOP, anchor=NW)
    T6.insert(INSERT,"","\n", '',"\n")
    fm6.pack(side=LEFT,anchor=NW)

def quit():
        print("quitting...")
        sys.exit(0)
def __init__(self):
    self.bind_all("<Control-q>", self.quit)
menu1 = Menu(v0)
v0.config(menu=menu1)
v0.title("MODELO DE PRONOSTICOS")
v0.geometry("1500x1500")
v0.config(bg="DodgerBlue3")



menu11= Menu(menu1, tearoff=0)
menu1.add_cascade(label="Archivo",underline=0, menu=menu11)
menu11.add_command(label="Lee-Arch",underline=0,command=lambda: leeArc(""))


"""menu12 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Matrez de Serie", menu=menu12)
menu12.add_command(label="Matriz-Suma Cuadrados",command=lambda: imprimir(m))
menu12.add_separator()"""

menu5 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Modelos",underline=0, menu=menu5)
menu5.add_command(label="Regresion lineal simple",underline=0,command=lambda:RLS(m,n))
menu5.add_command(label="Regresion lineal Multiple",underline=0,command=lambda:RLM(m, n,data))
menu5.add_command(label="Promedio Movil Simple",underline=0,command=lambda:fInterConfi(m,n))
menu5.add_command(label="Intervalos de Confianza",underline=0,command=lambda:InterConfi(m,n))

menu3 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Graficas",underline=1, menu=menu3)
menu3.add_command(label="Diagrama-Dispersion",underline=0,command=lambda:ventana(m))
menu3.add_command(label="Diag-Int-Conf",underline=0,command=lambda:finterComfiG(m,n))

menu1.add_command(label="Salir",underline=0, command=lambda:quit())

v0.mainloop()#!/usr/bin/env python
