#!/usr/bin/env python
#-*- coding: utf-8 -*
import os
import tkinter as tk
import numpy as np
from io import StringIO
from tkinter import filedialog


def leerArchivo():
    global n,m,data
    archivo =filedialog.askopenfilename() 
    z = open(archivo, 'r' )
    data=z.read()
    data=np.genfromtxt(StringIO(data))
    data=np.matrix(data)
    n=len(data)
    matriz= data[0:n]     
    m=matriz.transpose()
    #print ("data=",data)
    # print ("n=",len(data))
    z.close()
    return m,n,data

# leerArchivo()