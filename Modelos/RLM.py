from numpy import linalg
from tkinter import *
import tkinter as tk
import numpy as np
import scipy.stats as st
from io import StringIO
from tkinter import filedialog
from ArchivoPy3 import*

vec=[];vy=[];vyt=[]
mat=[]
a=0
import math

def fRlm(m,n,data):     
    vy=array(m[0:1]) # vector variable explicada
    yT=transpose(vy)#t
    suma=vy.sum()
    prom=suma/n
    x=array(data)#Archivo leido de texto convertido a array
    for i in range(0,len(data)):#LLenar la primera columna de la matriz "X"  con unos
        for j in range(0,len(data)):
            x[i][0]=1
 
    xT=np.transpose(x)#trasponer la matriz "X"
    A = matrix(data)#crea un objeto de la matriz original
    #print len(matT),len(matT[0])
    #print len(mat),len(mat[0])
    
    xTxc=np.zeros((len(xT),len(x[0])))

     
    for i in range(len(xT)):
        for j in range(len(xT[0])):
                       for k in range(len(x[0])):
                           xTxc[i][k]+=(xT[i][j]*x[j][k])
                           
    
    xTx=matrix(xTxc)
    xTxIn=xTx.I
    xTxInv=array(xTxIn)
    xyT=np.zeros((len(xT),len(yT[0])))
   
    for i in range(len(xT)):
        for j in range(len(xT[0])):
                       for k in range(len(yT[0])):
                           xyT[i][k]=xyT[i][k]+(xT[i][j]*yT[j][k])#multiplica xT por Y
   
    IxTxxyT=np.zeros((len(xTxInv),len(xyT[0])))
    
    
    for i in range(len(xTxInv[0])):
        for j in range(len(xTxInv[0])):
                       for k in range(len(xyT[0])):
                           IxTxxyT[i][k]+=(xTxInv[i][j]*xyT[j][k])

def fMatriVects(m,n,data):     
    vy=array(m[0:1]) # vector variable explicada
    yT=transpose(vy)#t
    suma=vy.sum()
    prom=suma/n
    x=array(data)#Archivo leido de texto convertido a array
    for i in range(0,len(data)):#LLenar la primera columna de la matriz "X"  con unos
        for j in range(0,len(data)):
            x[i][0]=1
 
    xT=np.transpose(x)#trasponer la matriz "X"
    A = matrix(data)#crea un objeto de la matriz original
    #print len(matT),len(matT[0])
    #print len(mat),len(mat[0])
    
    xTxc=np.zeros((len(xT),len(x[0])))

     
    for i in range(len(xT)):
        for j in range(len(xT[0])):
                       for k in range(len(x[0])):
                           xTxc[i][k]+=(xT[i][j]*x[j][k])
                           
    
    xTx=matrix(xTxc)
    xTxIn=xTx.I
    xTxInv=array(xTxIn)
    xyT=np.zeros((len(xT),len(yT[0])))
   
    for i in range(len(xT)):
        for j in range(len(xT[0])):
                       for k in range(len(yT[0])):
                           xyT[i][k]=xyT[i][k]+(xT[i][j]*yT[j][k])#multiplica xT por Y
   
    IxTxxyT=np.zeros((len(xTxInv),len(xyT[0])))
    
    
    for i in range(len(xTxInv[0])):
        for j in range(len(xTxInv[0])):
                       for k in range(len(xyT[0])):
                           IxTxxyT[i][k]+=(xTxInv[i][j]*xyT[j][k])

    xIxTxxyT=np.zeros((len(x),len(IxTxxyT[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
                       for k in range(len(IxTxxyT[0])):
                         xIxTxxyT[i][k]+=(x[i][j]*IxTxxyT[j][k])
    
    print("IxTxxyT=",IxTxxyT)
    
    return x,xT,xTx,xTxInv,xyT,IxTxxyT,xIxTxxyT,prom

def fReglinMul():
    x,xT,xTx,xTxInv,xyT,IxTxxyT=fMatriVects(m, n, data)
    k=0
    print ("Y=",",")  
    for i in range(len(xyT)):
        if i==0:
            print ( round( IxTxxyT[i][k],1),"+",)
        else:
            if  i==len(IxTxxyT)-1:
                print ( IxTxxyT[i][k],"X")
            else:
                print  (IxTxxyT[i][k],"X +",",")
    #print "B=",B

    return 

def fSCT(m,n):
    #x=array(data)#Archivo leido de texto convertido a array
    vy=array(m[0:1]) # vector variable explicada
    y=transpose(vy)#t
    suma=vy.sum()
    prom=suma/n
    va=array([(i-prom) for (i) in zip(vy)])
    yz=array([(i*j) for (i,j) in zip(va,va)])
    SCT=yz.sum()   
    return SCT,y

def fSCR(m,n,data):

    xIxTxxyT,prom=fMatriVects(m,n,data)
    yDD=[(i-prom) for (i) in zip(xIxTxxyT)]
    yD=[(i*j) for (i,j) in zip(yDD,yDD)]
    SCR=yD.sum()   
    return SCR
    
def fSCE(m,n):
    vy=array(m[0:1]) # vector variable explicada
    y=transpose(vy)#t
    x,xT,xTx,xTxInv,xyT,IxTxxyT,xIxTxxyT,prom=fMatriVects(m,n,data)
    yyP=[round((i-j),2) for (i,j) in zip(y,xIxTxxyT)]
    yP=[[(i*j) for (i,j) in zip(yyP,yyP)]] 
    SCE=yP.sum()
    return SCE

def fAnova(m,n):
    w=len(m)
    global MSE,Fc,S2
    SCT,y=fSCT(m,n)
    SCR=fSCR(m,n,data)#
    SCE=fSCE(m,n)
    MSE=SCR/1
    S2=SCE/(n-2)
    Fc=MSE/S2
    rc=1-(SCE/SCT)
    rcA=1-((SCE/(n-(w-1)-1))/(SCT/(n-1)))
    print("Anova=",SCT,SCR,SCE,MSE,S2,Fc)
    print( "rc)",rc)
    print( "w=",w)
    print ("rcA=",rcA)
    #div=SSR/S2
    #print"Anova=",SCT, SCR,SCE,MSE,S2,Fc
    return SCT# SCR,SCE,MSE,S2,Fc

m,n,data=leerArchivo()
fSCR(m,n,data)
#fAnova(m,n)
#fMatrices(m,n,data)
#fRlm(m,n,data)
#fAnova(m,n)