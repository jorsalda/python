from scipy.stats import norm
from scipy.stats import t
import math
import Tkinter
from numpy import *
from Tkinter import *
import Tkinter as tk
import numpy as np
from StringIO import StringIO 

def fProSuma():
    def donothing():
       print "a"
    
    def file_save():
        name=asksaveasfile(mode='R',defaultextension=".txt")
        text2save=str(text.get(0.0,END))
        name.write(text2save)
        name.close
    
    root = Tk()
    root.geometry("800x800+0+0")
    menubar=Menu(root)
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=file_save)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="Help",command=donothing)
    menubar.add_cascade(label="Help",menu=helpmenu)
    root.config(menu=menubar)
    
    
    
    text=Text(root,bg="black", height=5, width=200)
    text2=Text(root,bg="black", height=10, width=50)
    text.pack(side=TOP)
    text.pack()
    
    
    
    archivo=open("compleja.txt",'r')
    data=archivo.read()
    archivo.close()
    
    data=np.genfromtxt(StringIO(data)) #Se sobre entiende que los delimitadores son espacios
    data=np.matrix(data) #Transformar array de arrays en matriz
    matriz1 = data[0:31]
    #matriz2 = data[3:6]
    #matriz4=inv(matriz1) #inv determina la inversa
    b=matriz1.transpose()#determina la transpuesta de la matriz
    v1=array(b[0:1])
    v2=array(b[1:2])
    v3=array(b[2:3])
    v4=array(b[3:4])
    vect1=v1.transpose()
    vect2=v2.transpose()
    sumv1=vect1.sum()
    sumv2=vect2.sum()
    #xy  = [i*j for (i,j) in zip(v1,v2)]
    v11  = [i*i*i for (i,j) in zip(v1,v1)]#eleva cada uno de los elemntos al caudrado
    v22  = [i*i*i for (i,j) in zip(v2,v2)]
    v33  = [i*j for (i,j) in zip(v3,v3)]
    v44  = [i*j for (i,j) in zip(v4,v4)]#hallar un array con  el cuadrado de las posiciones de un vector
    v11=np.array(v11)#convierte  un array en un vector
    v1=np.array(v1)
    v22=np.array(v22)
    v33=np.array(v33)
    sumav11=v11.sum()
    sumav22=v22.sum()
    sumav33=v33.sum()
    #sumav44=v44.sum()
    
    
    
    
    
    ##T2 = Text(root, height=5, width=75)
    ##T2.pack(side=LEFT)
    
    root.config(bg="black")
    text.config(bg="black",fg="red")
    frame = tk.Frame(root, bg='black')
    frame.pack(fill='both', expand='yes')
    v1=tk.IntVar(value=0.0)
    v2=tk.IntVar(value=0.0)
    v3=tk.IntVar(value=0.0)
    
    Entry(textvariable=v2,bg="black", fg="red").place(x=20, y=100)
    Entry(textvariable=v3,bg="black", fg="red").place(x=20, y=120)
    
    def suma():
        suma=v2.get()+v3.get()
        v1.set(suma)
    
    def fwz():
        al=v2.get()
        val=(al/100)+(((1-(al/100))))/2
        z=norm.ppf(val)
        v1.set(fwz)
    
    
    def pro():
        a=len(b)
        print a
        prot=0.0
        i=0
        while i<=a-4:
            v1=array(b[0+i:4+i])
            vt=v1.transpose()
            sum1=v1.sum()
            pro=sum1/4
            prot=prot+pro
            print vt,"=",sum1,"Prom=",round(pro,2)
            i=i+1
    
    #label = tk.Label(frame, text="Total=",bg="black", fg="red").place(x=20, y=62)
    button = tk.Button(frame, text="Suma", bg='yellow',command=suma).place(x=20,y=62)
    wz = tk.Button(frame, text="wz", bg='yellow',command=fwz).place(x=20,y=102)
    Label(textvariable=v1,bg="black", fg="red").place(x=100, y=145)
    #Label(textvariable=v1,bg="black", fg="red").place(x=100, y=145)
    
    text.insert(INSERT, v11,"\n"," = ","+",sumav11)
    #text.insert(END,text2)
    
    
    root.mainloop()
fProSuma()