from numpy import linalg
from numpy import *
from Tkinter import *
import Tkinter as tk
import numpy as np
import scipy.stats as st
from StringIO import StringIO
import tkFileDialog
from Archivo import*

vec=[];vy=[];vyt=[]
mat=[]
a=0
import math



def fSCT(n,data):
    
    vy=array(m[0:1]) # vector variable explicada
    y=transpose(vy)#t
    suma=vy.sum()
    prom=suma/n
    va=array([(i-prom) for (i) in zip(vy)])
    yz=array([(i*j) for (i,j) in zip(va,va)])
    SCT=yz.sum()
    """print"vy=",vy
    print"prom=",prom
    print"va=",va
    print"SCT=",SCT"""
    return SCT
       
    
def fxT(data):
    x=array(data)#Archivo leido de texto convertido a array
    for i in range(0,len(data)):#LLenar la primera columna de la matriz "X"  con unos
        for j in range(0,len(data)):
            x[i][0]=1
    xT=np.transpose(x)#trasponer la matriz "X"    
    """print"x=",x
    print"xT=",x,xT"""
    return xT,x


def fxTxc():
    xT,x=fxT(data)
    xTxc=np.zeros((len(xT),len(x[0])))   
    for i in range(len(xT)):
        for j in range(len(xT[0])):
                       for k in range(len(x[0])):
                           xTxc[i][k]=xTxc[i][k]+(xT[i][j]*x[j][k])
                           
    xTx=matrix(xTxc)
    xTxIn=xTx.I
    xTxInv=array(xTxIn)
    """ print"xTx",xTxc
    print"mat",mat"""
    return xTxc,xTxInv

    #a= np.array(xTxc, dtype=int)     
def fxTy(data): 
    vy=array(m[0:1]) # vector variable explicada
    y=transpose(vy)#t
    x,xT=fxT(data)
    xTy=np.zeros((len(xT),len(y[0])))
    
    for i in range(len(xT)):
        for j in range(len(xT[0])):
                       for k in range(len(y[0])):
                           xTy[i][k]=xTy[i][k]+(xT[i][j]*y[j][k])#multiplica xT por Y
    return xTy
    
def fxTxInv(data):
    xTxc,xTxInv=fxTxc()
    xTy=fxTy(data)
    x,xT=fxT(data)
    B=np.zeros((len(xTxInv),len(xTy[0])))
    
    
    for i in range(len(xTxInv[0])):
        for j in range(len(xTxInv[0])):
                       for k in range(len(xTy[0])):
                           B[i][k]=B[i][k]+(xTxInv[i][j]*xTy[j][k])
    print"B",B
     
    return B
   
    #BB= np.array(B, dtype=float(0.0))  
                 
    for j in range(len(B[0])):
        s = 0
        for i in range(len(B)):
            #print "x[%d][%d] = %d" % (i, j, B[i][j])#imprmir que los elementos de un columna
            s += B[i][j]
       # print "La suma de la columna", j, "es", s
    print "Y=",  
    for i in range(len(xTy)):
        if i==0:
            print  round( B[i][k],1),"+",
        else:
            if  i==len(B)-1:
                print  B[i][k],"X"
            else:
                print  B[i][k],"X +",
   

    xD=np.zeros((len(x),len(B[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
                       for k in range(len(B[0])):
                         xD[i][k]+=(x[i][j]*B[j][k])
    print"xD=",xD  
    yDD=array([(i-prom) for (i) in zip(xD)])
    yD=array([(i*j) for (i,j) in zip(yDD,yDD)])
    SCR=yD.sum()
    print"SCR=",SCR
    return B
m,n,data=leerArchivo()
#fSCT(n,data)
#fxT(data)
#fxTxc()
#fxTy(data)
fxTxInv(data)