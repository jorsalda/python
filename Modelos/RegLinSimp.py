#!/usr/bin/env python
#-*- coding: utf-8 -*

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
from scr.RLS1 import*
from Archivo import*
from AppShell import*

z=0.0
bsum=0.0
def fRegLinSimp(m,n):#promedio movil simple
    root = Tk()
    root.geometry("800x800+800+200")
    root.config(bg="orange2")
    Pmw.initialise()
    nb = Pmw.NoteBook(root)
    p1 = nb.add('Analissi Preliminar')
    p2 = nb.add('Ajuste del Modelo')
    p5 = nb.add('Bondad de Ajuste2')
    p3 = nb.add('Bondad de Ajuste') 
    p4 = nb.add('Diagnóstioco del Modelo')
    
    nb.pack(padx=5, pady=5, fill=BOTH, expand=1)
    def fAnov5(m,n):
        SST,SSE,SSR,MSE,S2,Fc= fAnova(m,n)
        CME=fCME(m,n)
        r,rc,ra=fr(m,n)
        v5.create_text(w-150,h1-205,text="ANOVA",fill='black',font=('courier',10, 'bold')) 
        v5.create_line((w-400,h1-170),(w-0,h1-170))
        v5.create_line((w-400,h1-120),(w-0,h1-120))
        v5.create_line((w-265,h1-195),(w-265,h1-75))          
        v5.create_text(w-300,h1-180,text="Fuente",fill='purple',font=('courier',10, 'bold')) 
        
        v5.create_text(w-310,h1-35,text="Variables",fill='purple',font=('courier',10, 'bold')) 
        v5.create_text(w-310,h1-35,text="Variables",fill='purple',font=('courier',10, 'bold')) 
        v5.create_line((w-400,h1-20),(w-0,h1-20))# horizontal
        v5.create_line((w-400,h1),(w-0,h1))# horizontal
        v5.create_line((w-400,h1+20),(w-0,h1+20))# horizontal
        v5.create_line((w-265,h1-38),(w-265,h1+20)) # vertical  
        v5.create_line((w-265,h1-38),(w-265,h1+20)) # vertical 
        
        v5.create_line((w-200,h1-38),(w-200,h1+20)) # vertical          
        
        
        v5.create_text(w-240,h1-180,text="df",fill='blue',font=('courier',10, 'bold')) 
        v5.create_text(w-150,h1-180,text="SS",fill='blue',font=('courier',10, 'bold')) 
        v5.create_text(w-65,h1-180,text="MS",fill='blue',font=('courier',10, 'bold')) 
        v5.create_text(w+30,h1-180,text="F",fill='blue',font=('courier',10, 'bold'))
        v5.create_text(w+40,h1-180,text="(",fill='black',font=('courier',10, 'bold'))
        v5.create_text(w+120,h1-180,text="=",fill='black',font=('courier',10, 'bold'))
        v5.create_text(w+160,h1-180,text=round(Fc,2),fill='black',font=('courier',10, 'bold'))
        
        v5.create_text(w+58,h1-160,text="R-cuadra",fill='blue',font=('courier',10, 'bold'))
        v5.create_text(w+120,h1-160,text="=",fill='black',font=('courier',10, 'bold'))
        v5.create_text(w+160,h1-160,text=round(rc,4),fill='black',font=('courier',10, 'bold'))
        
        v5.create_text(w+58,h1-140,text="R-Ajus",fill='blue',font=('courier',10, 'bold'))
        v5.create_text(w+120,h1-140,text="=",fill='black',font=('courier',10, 'bold'))
        v5.create_text(w+160,h1-140,text=round(ra,4),fill='black',font=('courier',10, 'bold'))
        
        v5.create_text(w+50,h1-180,text=1,fill='black',font=('courier',8, 'bold'))
        v5.create_text(w+65,h1-180,text=",",fill='black',font=('courier',8, 'bold'))
        v5.create_text(w+80,h1-180,text=(n-2),fill='black',font=('courier',8, 'bold'))
        
         
        v5.create_text(w+100,h1-180,text=")",fill='black',font=('courier',10, 'bold'))
        
        
        v5.create_text(w-310,h1-155,text="Regresion",fill='blue',font=('courier',10, 'bold'))
        v5.create_text(w-310,h1-135,text="Resiudal",fill='blue',font=('courier',10, 'bold'))
        v5.create_text(w-310,h1-105,text="Total-Cor",fill='blue',font=('courier',10, 'bold'))
        
        v5.create_text(w-150,h1-160,text=round(SSR,2),fill='black',font=('courier',8, 'bold'))
        v5.create_text(w-145,h1-135,text=round(SSE,2),fill='black',font=('courier',8, 'bold'))
        v5.create_text(w-150,h1-105,text=round(SST,2),fill='black',font=('courier',8, 'bold'))
        
        v5.create_text(w-240,h1-160,text=1,fill='black',font=('courier',8, 'bold'))
        v5.create_text(w-240,h1-135,text=round(n-2),fill='black',font=('courier',8, 'bold'))
        v5.create_text(w-240,h1-105,text=round(n-1),fill='black',font=('courier',8, 'bold'))
        
        v5.create_text(w-60,h1-160,text=round(SSR,2),fill='black',font=('courier',8, 'bold'))
        v5.create_text(w-55,h1-135,text=round(S2,2),fill='black',font=('courier',8, 'bold'))
        v5.create_text(w-55,h1-105,text=round((SST/(n-1)),2),fill='black',font=('courier',8, 'bold'))
        
        
        
        
    def fAnov(m,n):
        SST,SSE,SSR,MSE,S2,Fc= fAnova(m,n)
        CME=fCME(m,n)
        r,rc,ra=fr(m,n)
        v3.create_text(w-150,h1-205,text="ANOVA",fill='black',font=('courier',10, 'bold')) 
        v3.create_line((w-400,h1-170),(w-0,h1-170))
        v3.create_line((w-400,h1-120),(w-0,h1-120))
        v3.create_line((w-265,h1-195),(w-265,h1-75))          
        v3.create_text(w-300,h1-180,text="Fuente",fill='purple',font=('courier',10, 'bold')) 
        
        
        v3.create_text(w-240,h1-180,text="df",fill='blue',font=('courier',10, 'bold')) 
        v3.create_text(w-150,h1-180,text="SS",fill='blue',font=('courier',10, 'bold')) 
        v3.create_text(w-65,h1-180,text="MS",fill='blue',font=('courier',10, 'bold')) 
        v3.create_text(w+30,h1-180,text="F",fill='blue',font=('courier',10, 'bold'))
        v3.create_text(w+40,h1-180,text="(",fill='black',font=('courier',10, 'bold'))
        v3.create_text(w+120,h1-180,text="=",fill='black',font=('courier',10, 'bold'))
        v3.create_text(w+160,h1-180,text=round(Fc,2),fill='black',font=('courier',10, 'bold'))
        
        v3.create_text(w+58,h1-160,text="R-cuadra",fill='blue',font=('courier',10, 'bold'))
        v3.create_text(w+120,h1-160,text="=",fill='black',font=('courier',10, 'bold'))
        v3.create_text(w+160,h1-160,text=round(rc,4),fill='black',font=('courier',10, 'bold'))
        
        v3.create_text(w+58,h1-140,text="R-Ajus",fill='blue',font=('courier',10, 'bold'))
        v3.create_text(w+120,h1-140,text="=",fill='black',font=('courier',10, 'bold'))
        v3.create_text(w+160,h1-140,text=round(ra,4),fill='black',font=('courier',10, 'bold'))
        
        v3.create_text(w+50,h1-180,text=1,fill='black',font=('courier',8, 'bold'))
        v3.create_text(w+65,h1-180,text=",",fill='black',font=('courier',8, 'bold'))
        v3.create_text(w+80,h1-180,text=(n-2),fill='black',font=('courier',8, 'bold'))
        
         
        v3.create_text(w+100,h1-180,text=")",fill='black',font=('courier',10, 'bold'))
        
        
        v3.create_text(w-310,h1-155,text="Regresion",fill='blue',font=('courier',10, 'bold'))
        v3.create_text(w-310,h1-135,text="Resiudal",fill='blue',font=('courier',10, 'bold'))
        v3.create_text(w-310,h1-105,text="Total-Cor",fill='blue',font=('courier',10, 'bold'))
        
        v3.create_text(w-150,h1-160,text=round(SSR,2),fill='black',font=('courier',8, 'bold'))
        v3.create_text(w-145,h1-135,text=round(SSE,2),fill='black',font=('courier',8, 'bold'))
        v3.create_text(w-150,h1-105,text=round(SST,2),fill='black',font=('courier',8, 'bold'))
        
        v3.create_text(w-240,h1-160,text=1,fill='black',font=('courier',8, 'bold'))
        v3.create_text(w-240,h1-135,text=round(n-2),fill='black',font=('courier',8, 'bold'))
        v3.create_text(w-240,h1-105,text=round(n-1),fill='black',font=('courier',8, 'bold'))
        
        v3.create_text(w-60,h1-160,text=round(SSR,2),fill='black',font=('courier',8, 'bold'))
        v3.create_text(w-55,h1-135,text=round(S2,2),fill='black',font=('courier',8, 'bold'))
        v3.create_text(w-55,h1-105,text=round((SST/(n-1)),2),fill='black',font=('courier',8, 'bold'))
        
        v3.create_line((w-400,h1-20),(w-0,h1-20))
        v3.create_line((w-400,h1),(w-0,h1))
        v3.create_line((w-265,h1-25),(w-265,h1+20))          
        v3.create_text(w-300,h1-40,text="Variables",fill='purple',font=('courier',10, 'bold')) 
        
        
    def fhipo():
        tbo=fEstPrue(m,n)
        T,df=fDistt(n)
        v2.create_text(w+25,h1+215,text="ANALISIS DE HIPOTESIS PARA LA PENDIENTE",fill='black',font=('courier',10, 'bold'))
        v2.create_text(w+200,h1+215,text="b",fill='blue',font=('courier',10, 'normal'))

        v2.create_text(w-153,h1+235,text="HO: b=0:'La pendiente es giual a cero'",fill='black',font=('courier',10, 'normal'))
        v2.create_text(w-128,h1+250,text="H1: b#0:'La pendidente es diferente de cero'",fill='black',font=('courier',10, 'normal'))
        if abs((round(T,3)))<abs((round(tbo,3))):
            v2.create_text(w-78,h1+265,text="Se rechaza H0 porque | t0 |>ta/2, es decir: "+str(abs((round(tbo,3))))+" > "+str(abs((round(T,3)))),fill='black',font=('courier',10, 'normal'))
            v2.create_text(w-140,h1+280,text="por consiguinte b es diferente de cero y  ",fill='black',font=('courier',10, 'normal'))
            v2.create_text(w+135,h1+280,text="EL MODELO  ES FUNCIONAL. ",fill='BLUE',font=('verdena',10, 'bold'))

        else:
            v2.create_text(w-65,h1+265,text="NO se rechaza H0 porque | t0 |<ta/2, es decir: "+str(abs((round(tbo,3))))+" < "+str(abs((round(T,3)))),fill='black',font=('courier',10, 'normal'))
            v2.create_text(w-140,h1+280,text="por consiguite b es diferente de cero y  ",fill='black',font=('courier',10, 'normal'))
            v2.create_text(w+135,h1+280,text="EL MODELO NO ES FUNCIONAL. ",fill='RED',font=('verdena',10, 'bold'))
                 
    def fShell():
        global z
        z=fAppshell() 
        v1.create_text(w-140,h1+280,text=z,fill='black',font=('courier',10, 'normal'))
        
    def fShell2(z):        
        v1.create_text(w-40,h1+280,text=z,fill='black',font=('courier',10, 'normal'))
        
    def fAjuste():
        tbo=fEstPrue(m,n)
        veyzz,vey,vexaa=fIntConf(m,n)
        T,df=fDistt(n)
        v2.create_text(w,h1-220,text="Ajuste del Modelo",fill='orange2',font=('verdena', 12, 'bold'))
        v2.create_text(w-180,h1-180,text="Intervalo de confianza serie histórica",fill='black',font=('verdena', 10, 'bold'))
        v2.create_line((w-320,h1-170),(w-40,h1-170))
        v2.create_text(w+20,h1-160,text="Int-Sup="+str(veyzz),fill='black',font=('courier', 8, 'bold'))
        v2.create_text(w-20,h1-145,text="Ser-hist="+str(vey),fill='black',font=('courier', 8, 'bold'))
        v2.create_text(w+10,h1-130,text="Int-Inf="+str(vexaa),fill='black',font=('courier', 8, 'bold'))
        v2.create_line((w-320,h1-120),(w-100,h1-120))
          
        v2.create_text(w-160,h1-90,text="Intervalo de confianza serie en Pronóstico",fill='black',font=('verdena', 10, 'bold'))
        v2.create_line((w-320,h1-80),(w-40,h1-80))
        v2.create_text(w+20,h1-70,text="Int-Sup="+str(veyzz),fill='black',font=('courier', 8, 'bold'))
        v2.create_text(w-20,h-55,text="Ser-hist="+str(vey),fill='black',font=('courier', 8, 'bold'))
        v2.create_text(w+10,h1-40,text="Int-Inf="+str(vexaa),fill='black',font=('courier', 8, 'bold'))
        v2.create_line((w-320,h1-25),(w-100,h1-25))
        
        v2.create_text(w+10,h1-10,text="Contraste de Hipótesis",fill='orange2',font=('verdena', 12, 'bold'))
        v2.create_line((w-320,h1+5),(w+400,h1+5))
        v2.create_text(w-126,h1+20,text="Si b1=0, ó r=0, entoces 'X' no explica 'Y'.  ",fill='black',font=('courier',10, 'normal'))
        v2.create_text(w-85,h1+35,text="La Región de rechazo está dada por | t0 |>ta/2.  Donde:",fill='black',font=('courier',10, 'normal'))
        v2.create_text(w-156,h1+50,text="|t0|: Estadístico de prueba =",fill='black',font=('courier',10, 'normal'))
      
        v2.create_text(w-190,h1+65,text="Grados de libertad =",fill='black',font=('courier',10, 'normal'))
        v2.create_text(w-50,h1+75,text="ta/2:valor de tabla t-studen con n-2 grado de libertad:",fill='black',font=('courier',10, 'normal'))
        v2.create_text(w+10,h1+90,text="Para un intervalo de confinaza del 95%, el nivel de significancia es  (1-a)=5%",fill='black',font=('courier',10, 'normal'))
        v2.create_text(w+10,h1+105,text="ó 0.05 y a/2 es de 0.025. Una distribucion T-studen con n-2 grados de libertad",fill='black',font=('courier',10, 'normal'))
        
        v2.create_text(w,h1+50,text=str(abs((round(tbo,3)))),fill='orange2',font=('verdena',12, 'bold'))
        v2.create_text(w-85,h1+65,text=df,fill='orange2',font=('verdena',12, 'bold'))
        v2.create_text(w+190,h1+75,text=str(abs((round(T,3)))),fill='orange2',font=('verdena',12, 'bold'))
        
        
        

    def grafica(m):        
        vx=array(m[0:1])
        vy=array(m[1:2])
        yt=vy.transpose()
        xt=vx.transpose()
        
        root.title('Regresiion Lineal')
        
        v1.pack(side=RIGHT,anchor=SE)
        
        v1.create_line(100,250,400,250, width=2)
        v1.create_line(100,250,100,50, width=2)
        
        for i in range(11):
            x = 100 + (i * 30)
            v1.create_line(x,250,x,246, width=2)
            v1.create_text(x,254, text='%d'% (10*i), anchor=N)
        
        for i in range(6):
            y = 250 - (i * 40)
            v1.create_line(100,y,105,y, width=2)
            v1.create_text(96,y, text='%5.1f'% (50.*i), anchor=E)
        vye= [num for elem in yt for num in elem]
        vxe= [num for elem in xt for num in elem]
        
        vyx  = [(i,j)for (i,j) in zip(vye,vxe)]
        print( vyx)
        for x,y in vyx:
            x = 100 + 3*x
            y = 250 - (4*y)/5
            v1.create_oval(x-0.2,y-0.2,x+2,y+2, width=1, outline='blue', fill='SkyBlue2')
    
  
    def fCMEe2(m,n):     
        a,b=modeloRLS(m,n)
        r,rc,ra=fr(m,n)
        
        v1.create_text(w-255,h1+40,text="Modelo Lineal",fill='black',font=('verdena', 10, 'bold'))
        v1.create_line((w-320,h1+50),(w-200,h1+50))
        v1.create_text(w-260,h1+60,text="Y="+str(round(a,2))+"+"+str(round(b,2))+"x",fill='orange2',font=('Verdana', 10, 'bold'))
          
        
        v1.create_line((w-320,h1+70),(w-200,h1+70))
        v1.create_line((w-320,h1+71),(w-200,h1+71))
        
        
        v1.create_text(w-210,h1+110,text="Coeficiente de correlacion",fill='black',font=('Verdana',10,'bold'))
        v1.create_line((w-320,h1+120),(w,h1+120))
        v1.create_text(w-280,h1+131,text="r="+str(round(r,2)),fill='orange2',font=( 'Verdena', 10, 'bold'))
        v1.create_text(w-60,h1+150,text="El valor :  "+str(round(r,2))+" establece que 'X',explica a 'Y' en un  "+str(round(r,2)*100)+"%,",fill='black',font=('courier', 9, 'normal'))
        v1.create_text(w-170,h1+165,text="lo que significa un buen modelo",fill='black',font=('courier', 9, 'normal'))
        
        v1.create_line((w-320,h1+175),(w,h1+175))
        v1.create_line((w-320,h1+176),(w,h1+176))
        
        return 
    
    v1=Canvas(p1)
    w = v1.winfo_reqwidth()
    h1 = v1.winfo_reqheight()
    fCMEe2(m,n)
    grafica(m)
    v1.pack(fill=BOTH, expand=1) 
    
    v2 = Canvas(p2)# bg='gray30'
    w = v2.winfo_reqwidth()
    h = v2.winfo_reqheight()
    fAjuste()
    fhipo()
    v2.pack(fill=BOTH, expand=1) 
    
    v3 = Canvas(p3)# bg='gray30'
    w = v3.winfo_reqwidth()
    h = v3.winfo_reqheight()
    global bsum
    #fAnov(m,n)
    bsum=Button(v1,command=fShell,text='Z_Acumulada',padx=2,pady=5).place(x=50,y=455)#bonto para ingresar valor Z
    #bsum=Button(v1,command=fShell2(z),text='Z_Acumulada',padx=2,pady=5).place(x=0,y=55)#bonto para ingresar valor Z
    
    v3.pack(fill=BOTH, expand=1) 
    
    
    v5 = Canvas(p5)# bg='gray30'
    w = v5.winfo_reqwidth()
    h = v5.winfo_reqheight()
    fAnov5(m,n)
    v5.pack(fill=BOTH, expand=1) 

    
    def fCMEe3(m,n):     
        a,b=modeloRLS(m,n)
        w.create_text(t-420,g-420,text="(F",fill='black',font=('currier', 8, 'bold'))
        w.create_text(t-240,g-300,text=1,fill='black',font=('currier', 8, 'bold'))
        w.create_text(t-220,g-300,text=(n-2),fill='black',font=('currier', 8, 'bold'))
        
        w.create_text(t-210,g-300,text=")",fill='black',font=('currier', 8, 'bold'))
       # w.create_text(t-250,g-360,tett=")",fill='black',font=('Verdana', 12, 'bold'))
        w.create_text(t-250,g-250,text="Moddlo Lineal",fill='black',font=('Verdana', 12, 'bold'))
        w.create_text(t-280,g-230,text="Y=",fill='red',font=('Verdana', 8, 'bold'))
        w.create_text(t-250,g-230,text=round(a,2),fill='black',font=('Verdana', 8, 'bold'))
        
        return 
    
    w = Canvas(p3, width=450, height=500, borderwidth=2,background='white', relief='raised')
    t=w.winfo_reqwidth()
    g=w.winfo_reqheight()
    
    fCMEe3(m,n)# IMPRIME EN UN CANVAS
    w.pack(side=RIGHT,anchor=NE)
    v3.pack(fill=BOTH, expand=0) 
    root.mainloop()
    

"""fRegLinSimp(m,n)
m,n,data=leerArchivo()"""
