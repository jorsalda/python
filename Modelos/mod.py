#!/usr/bin/env python
#-*- coding: utf-8 -*
import os
import Tkinter
from numpy import *
from Tkinter import *
import Tkinter as tk
import numpy as np
from StringIO import StringIO 
import matplotlib.pyplot as grafico
import tkFileDialog
from RLSC import*

m=0;n=0;data=0;vy=0;vx=0;a=0;b=0

v0=Tk()
    
def leeArc(self):
    global n,m,data
    archivo = tkFileDialog.askopenfilename()
    a = open(archivo, 'r' )
    data=a.read()
    data=np.genfromtxt(StringIO(data))
    data=np.matrix(data)
    n=len(data)
    matriz= data[0:n]     
    m=matriz.transpose()
    a.close()
    return m,n,data

def ventana(m):
    global vy
    global vx
    vy=array(m[0:1])
    vx=array(m[1:2])
   
    grafico.scatter(vy, vx)
    grafico.gray()
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

def RLM(m,n):
    v1 = Tk() # Tk() Es la ventana principal
    
    v1.config() # Le da color al fondo
    v1.geometry("800x800+600+600") # Cambia el tamaño de la ventana y la posicion
    
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
        CME=fCME(m,n)
        r,rc,ra=fr(m,n)
        
        Label(v1, text="Anova:", fg="blue").place(x=280, y=200)
        Label(v1, text="Fuente", fg="purple").place(x=60, y=220)
        Label(v1, text="df:", fg="blue").place(x=150, y=220)
        Label(v1, text="ss:", fg="blue").place(x=210, y=220)
        Label(v1, text="MS:", fg="blue").place(x=305, y=220)
        Label(v1, text="fc:", fg="blue").place(x=380, y=220)
        Label(v1, text="-----------------------------------------------------------------------", fg="white").place(x=140, y=235)
        Label(v1, text="Regresión", fg="purple").place(x=60, y=255)
        Label(v1, text=round(SSR,2), fg="black").place(x=210, y=255)
        Label(v1, text="Residual", fg="purple").place(x=60, y=280)
        Label(v1, text=round(SSE,2), fg="black").place(x=210, y=280)
        Label(v1, text=round(MSE,2), fg="black").place(x=305, y=255)
        Label(v1, text=round(S2,2), fg="black").place(x=305, y=275)
        Label(v1, text=round(Fc,2), fg="black").place(x=380, y=255)
        
        Label(v1, text="total-Corr", fg="purple").place(x=60, y=300)
        Label(v1, text= 1, fg="black").place(x=160, y=255)
        Label(v1, text=round(SST,2), fg="black").place(x=210, y=300)
        
        Label(v1, text=(n-2), fg="black").place(x=160, y=280)
        Label(v1, text=(n-1), fg="black").place(x=160, y=300)
        Label(v1, text=round((SST/(n-1)),3), fg="black").place(x=305, y=300)
        btnIng=Button(v1,text="entrar",font=("Agency FB",14),width=5).place(x=420, y=300)
        Label(v1, text="Error-Estan", fg="purple").place(x=60, y=340)
        Label(v1, text=round(CME,3), fg="black").place(x=160, y=340)
        Label(v1, text="r-Cuad", fg="purple").place(x=60, y=360)
        Label(v1, text=round(rc,3), fg="black").place(x=160, y=360)
        
        Label(v1, text="Coef-Co:r=", fg="purple").place(x=60, y=380)
        Label(v1, text=round(r,2), fg="black").place(x=160, y=380)
        Label(v1, text="Coef-do:rc:=", fg="purple").place(x=60, y=400)
        Label(v1, text=round(rc,2), fg="black").place(x=160, y=400)  
        
        
        
          
    def SCuadrados():
        sxx,syy,sxy= fScuad(m,n)
        r=fr(m,n)
        Label(v1, text="SUMDA CUDRADOS:", fg="blue",font=("Agency FB",12)).place(x=180, y=430)
        Label(v1, text="Sxx", fg="red").place(x=60, y=455)
        Label(v1, text="Syy", fg="red").place(x=200, y=455)
        Label(v1, text="Sxy", fg="red").place(x=340, y=455)

        Label(v1, text=round(sxx,2), fg="red").place(x=60, y=475)
        Label(v1, text=round(syy,2), fg="red").place(x=200, y=475)
        Label(v1, text=round(sxy,2), fg="red").place(x=340, y=475)
        
    def fEstaPrue(m,n):
        tbo=fEstPrue(m,n)
        T,df=fDistt(n)
        Label(v1, text="Prueba Hipotesis b1", font=("Agency FB",12),fg="blue").place(x=400, y=500)
        Label(v1, text="Si b1=0, ó r=0 --> X no explica Y", fg="black").place(x=60, y=520)
        Label(v1, text="Regiogn de rechazo, | t0 |>ta/2=",fg="black").place(x=60, y=540) 
        Label(v1, text=abs((round(T,3))), fg="red").place(x=260, y=540) 
        Label(v1, text="grados de libertad", fg="black").place(x=60, y=560)
        Label(v1, text=df, fg="red").place(x=260, y=560)
        Label(v1, text="Estadística de prueba", fg="black").place(x=60, y=580)
        Label(v1, text=round(tbo), fg="red").place(x=260, y=580)
        
        
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
    
    
    def uno():
        print"JORGE SALDARRIGA!"
   
    menu2 = Menu(v1)
    v1.config(menu=menu2)
    v1.title("Regresión lienal simple")
    menu11 = Menu(menu2, tearoff=0)
    menu2.add_cascade(label="Archivo", menu=menu11)
    menu11.add_command(label="Lee-Arch",command=lambda: leeArc(""))
    
    
    menu1_2 = Menu(menu2, tearoff=0)
    menu2.add_cascade(label="Serie-T", menu=menu1_2)
    menu1_2.add_command(label="Matriz",command=lambda: imprimir(m))
    menu1_2.add_command(label="Est-Prueba",command=lambda:fEstaPrue(m,n))
    menu1_2.add_command(label="Rls",command=lambda: ModRLS(m,n))
    menu1_2.add_command(label="co-corre",command=lambda: uno())
    menu1_2.add_command(label="NP")
    menu1_2.add_command(label="Anova",command=lambda:Anova(m,n))
    menu1_2.add_command(label="Scuadrados",command=lambda:SCuadrados())

    menu2.add_cascade(label="correlacion", menu=menu12)
    
    menu2.add_command(label="Salir", command=v1.quit)
    #menu1_1_1 = Menu(menu2, tearoff=0)
    v1.mainloop() # Es el evento que llama al inicio de nuestro programa. Siempre lo lleva la ventana principal.

def imprimir(data):
    os.system('clear')
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

menu1 = Menu(v0)
v0.config(menu=menu1)
v0.title("MODELO DE PRONOSTICOS")
v0.geometry("1500x1500")
v0.config(bg="black")



menu11= Menu(menu1, tearoff=0)
menu1.add_cascade(label="Archivo", menu=menu11)
menu11.add_command(label="Lee-Arch",command=lambda: leeArc(""))


menu12 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Serie-T", menu=menu12)
menu12.add_command(label="Matriz",command=lambda: imprimir(m))
menu12.add_command(label="Anova",command=lambda: imprimir(m))
menu12.add_separator()

menu121 = Menu(menu12, tearoff=0)
menu12.add_cascade(label="Operaciones", menu=menu121)
menu121.add_command(label="Matriz",command=lambda: ModRLS(a,b))
menu121.add_command(label="Suma",command=lambda: imprimi(m))
menu121.add_command(label="Rls",command=lambda: ModRLS(m,n))
menu121.add_command(label="Anova",command=lambda:Anova(m,n))
menu121.add_command(label="Scuadrados",command=lambda:SCuadrados())


menu4 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Correlaciones", menu=menu4)
menu4.add_command(label="Coefi-Corr: r",command=lambda:rc())


    
menu5 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Modelos-Pronosticos", menu=menu5)
menu5.add_command(label="Regresion lineal simple",command=lambda:RLM(m,n))



menu3 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Graficas", menu=menu3)
menu3.add_command(label="Diagrama-Dispersion",command=lambda:ventana(m))

menu1.add_command(label="Salir", command=v0.quit)
v0.mainloop()#!/usr/bin/env python
