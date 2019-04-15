#!/usr/bin/env python
#-*- coding: utf-8 -*
import os
import Tkinter as tk
import numpy as np
from StringIO import StringIO
import tkFileDialog


def leerArchivo():
    global n,m,data
    archivo = tkFileDialog.askopenfilename()
    z = open(archivo, 'r' )
    data=z.read()
    data=np.genfromtxt(StringIO(data))
    data=np.matrix(data)
    n=len(data)
    matriz= data[0:n]     
    m=matriz.transpose()
    
    z.close()
    if n==1:
        n=len(m) 
        """for i in range(0,len(data)):#LLenar la primera columna de la matriz x con unos
            for j in range(0,len(data)):
                data[0][j]=1  
        vx=vx.transpose()"""
        m=m.transpose()
    # print "data=",data
    return m,n,data
