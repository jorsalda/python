#!/usr/bin/env python
#-*- coding: utf-8 -*
import os
import tkinter as tk
import numpy as np
import matplotlib.pyplot as grafico
from scipy.stats import norm
from scipy.stats import t
import math
from ArchivoPy3 import *
# Definción de variables. 
j=0;i=0;R=0;ra=0;m=0;n=0;a=0;b=0;vy=0;svyt=0;svy=0;vyp=0;vyct=0;svyc=0;var=0;desv=0;intif=0;intsu=0
vx=0;VYSST=0;vycSST=0;vySSE=0;SST=0;vyctp=0;vycp=0;vx=0;svx=0;vxt=0
vxct=0;svxc=0;syy=0;vectores=0;vxy=0;sxx=0;vxyt=0;svxy=0;vxyct=0;svxyc=0
vxxyy=0;svxyc=0;sxy=0;CME=0;px=0;py=0;r=0;rc=0;tbo=0;T=0
vex=0;vexa=0;vexaa=0;vey=0;veyz=0;veyzz=0
SSR=0;SCE=0;SCR=0;SSE=0;SSTx=0;MSE=0;Fc=0;S2=0
vyc=[];ve=[];vx=[];vy=[];v=[];vyt=[] ; vyy=[];vyyc=[];vcprod=[]
vcprodc=[]


def fvy(m):
    global vy,vyt 
    suma=0
    vx=np.array(m[0:1])
    svy=vx.sum()   
    vyt=np.transpose(v)
    vyy  = [(i*j) for (i,j) in zip(vy,vy)]#Vector "y" al cuadarado.+++
    vyc  = np.array(vyy)
    
    
    # print("sin corchetes este: ",vy)
    # print("vector transpuesto: ",vyt)
    # print("vector al cuadrado: ",vyyc)
    # print("vector producto transpuesto: ",vcprodc)
    # print("suma ",svyt)
    return vy,svy,vyt,vyc  


def fvx(m):
    global vx,vxt
    vx=np.array(m[1:2])
    svx=vx.sum()  
    vxt=np.transpose(v) 
    vxx  = [(i*j) for (i,j) in zip(vx,vx)]#Vector "y" al cuadarado.+++
    vxc  = np.array(vxx)
    # print("sin corchetes este: ",vx)
    # print("vector transpuesto: ",vxt)
    # print("vector al cuadrado: ",vxc)
    # print("suma ",svxt)
    # vx=np.array(m[1:2])
    # vxt=vx.transpose()
    # print("vec X",vx)
    # print("vec X trans",vxt)
    return vx,svx,vxt,vxc

    
# def vectory(m,n):
#     global svy, vyct, svyc
#     vy,vyt=fvy(m)
#     v=[num for elem in vy for num in elem]
#     vyy  = [(i*j) for (i,j) in zip(v,v)]#Vector "y" al cuadarado.
#     svy=vy.sum()
#     print("vactor original",v)
#     print("vactor al cuadrado",vyy)
#     return svy,vyct,svyc
    
# def vectorx(m,n):
#     global svx, vxct,svxc,promx
#     vx,vxt=fvx(m)
#     v=[num for elem in vx for num in elem]
#     vxt=vx.transpose()
#     vxx  = [i*i for (i,j) in zip(v,v)]#Vector "x" al cuadarado.
#     svx=vx.sum()
#     vxc=np.array(vxx)
#     vxct=vxc.transpose()
#     svxc=vxc.sum()
#     print("vector x al cuadrado:", vxx)
#     print("vector x al cuadrado:", vxc)
#     return svxc,svx,vxct
        
def vectorxy(m):
    vx,vxt,vxc=fvx(m)
    vy,vyt,vyc=fvy(m)
    avxy  = [i*j for (i,j) in zip(vy,vx)]
    vxy=np.array(avxy)
    vxyt=vxy.transpose()
    svxy=vxy.sum()
    print("vector x:", vx)
    print("vector y :", vy)
    print("vector xy :", avxy)
    print(" usma del vector xy:", svxy)
    return  svxy,vxyt
  
def modeloRLS(m,n): 
    global a,b
    vy=np.array(m[0:1])
    vx=np.array(m[1:2])   
    vyt=vy.transpose()  
    vxt=vx.transpose()
    svy=vyt.sum()
    svx=vxt.sum()    
    vyy  = [i*i for (i,j) in zip(vy,vy)]#Vector "y" al cuadarado.
    vyc=np.array(vyy)
    vyct=vyc.transpose()
    svyc=vyc.sum()
    vxx  = [i*i for (i,j) in zip(vx,vx)]#Vector "y" al cuadarado.
    vxc=np.array(vxx)
    vxct=vxc.transpose()
    svxc=vxct.sum()
    avxy  = [i*j for (i,j) in zip(vy,vx)]
    vxy=np.array(avxy)
    vxyt=vxy.transpose()
    svxy=vxy.sum()
    b=(n*svxy-(svy*svx))/(n*svxc-(svx**2))
    a=(svxc*svy-(svx*svxy))/(n*svxc-(svx**2))
   
    return a,b

def fr(m,n): 
    "coeficiente de determinacion r; r cuadruado y r ajustado"
    global r,rc
    vy,vyt,vyc=fvy(m)
    vx,vxt,vxc=fvx(m)
    # vyt=vy.transpose()  
    # vxt=vx.transpose()
    svy=vyt.sum()
    svx=vxt.sum()        
    vyy  = [i*i for (i,j) in zip(vy,vy)]#Vector "y" al cuadarado.
    vyc=np.array(vyy)
    vyct=vyc.transpose()
    svyc=vyc.sum()    
    vxx  = [i*i for (i,j) in zip(vx,vx)]#Vector "y" al cuadarado.
    vxc=np.array(vxx)
    vxct=vxc.transpose()
    svxc=vxct.sum()
    avxy  = [i*j for (i,j) in zip(vy,vx)]
    vxy=np.array(avxy)
    vxyt=vxy.transpose()
    svxy=vxy.sum()
    r  = (n*svxy-svx*svy)/math.sqrt((n*svxc-svx**2)*(n*svyc-svy**2))
    rc=r**2    
    ra=1-((float((n-1))/(n-2))*(1-rc))
    print("r=",(round(r,4)))
    print("rc=", (round(rc,4)))
    print("ra=",(round(ra,4)))
    
    return r,rc,ra

def fSS(m,n):
    global svy, vyct, svyc
    vy=np.array(m[0:1]) 
    vyt=vy.transpose()
    svy=vyt.sum()
    vyp=svy/n   
    vySS  = [i-vyp for (i) in zip(vy)]#Vector "residuos" .
    vycSS  = [i*i for (i,j) in zip(vySS,vySS)]#Vector "residuos" al cuadarado.
    vycp=np.array(vySS)
    vyctp=vycp.transpose()
    vycpp=np.array(vycSS)
    vyctpp=vycpp.transpose()
    SS=vycpp.sum() 
    print ("vySS=",vyctp)
    print ("SS=",SS)
    return SS

def fSSTx(m,n):
    
    global svxc,svx,vxct,SSTx
    vx=np.array(m[1:2]) 
    vxt=vx.transpose()
    svx=vxt.sum()
    vxp=svx/n   
    SSTx  = [i-vxp for (i) in zip(vx)]#Vector "residuos" .
    vxcSST  = [i*i for (i,j) in zip(SSTx,SSTx)]#Vector "residuos" al cuadarado.
    vxcp=np.array(vxcSST)
    vxctp=vxcp.transpose()
    vxcpp=np.array(vxcSST)
    vxctpp=vxcpp.transpose()
    SSTx=vxcpp.sum() 
    print (SSTx)
    return SSTx

def fDW(m,n):
    i=0
    SSE,vySSE=fSSE(m,n)
    while i<=n-2:
        v1=np.array(vySSE[0+i:2+i])    
        sum1=v1.sum()
        ve.insert(i,sum1)
        sum1=0
        i=i+1
    #vec=array(ve)
    
    vyy  = [i*i for (i,j) in zip(ve,ve)]
    svyy=np.array(vyy)
    ssvyy=svyy.sum()
    print (svyy)

def fCME(m,n):
    global CME
    SSE=fSSE(m, n)
    CME=(SSE/(n-2))
    #print"CME>>",CME
    #print"cme", CME
 
    return CME

def fprom(m,n):#realiza el promeido de las variables X,Y
    global px,py
    vx,svx,vxt,vxc=fvx(m)
    vy,svy,vyt,vyc=fvy(m)    
    px=svx/n
    py=svy/n
    print("promedio en x",round(px,2))
    print("promedio en y",round(py,2))
    return py,svy,svy,svyc
   
def fsxx(m,n):# sumatoria del vector "Y" al cuadrado
    global sxx
    svxc,svx,vxct=fvx(m)
    sxx=svxc-((svx**2)/n)
    #print"sxx",sxx
    return sxx

def fsyy(m,n):
    svxc,svx,vxct=fvy(m)
    syy=svyc-((svy**2)/n)
    #print"syy=", syy
    return syy

def fsxy(m,n):#sumatoria de vecx[] por vcey[]
    svxc,svx,vxct=fvy(m)
    svxy,vxyt=vectorxy(m)
    svxc,svx,vxct=fvx(m)
    sxy=svxy-((svy*svx)/n)
    print ("sxy=",sxy)
    return sxy
def fSSE(m,n):
    # SCE: suma del cuadrado del error(valor residual del error)
    global SSE
    a,b=modeloRLS(m,n)
    syy=fsyy(m,n)
    sxy=fsxy(m,n)
    SSE=syy-b*sxy  
    #print "SSE=",SSE
    #print "CME=",CME
    #print "y-y'=",vySSE# calcular el error estandar
    #print "y-3'=",(vySSE[0][3:5]) 
    return SSE

def ferrorEstandar(m,n):
    "Error estandar de estimancion"
    CMEE=fCME(m, n)
    CME=math.sqrt(CMEE)
    print("errrrooEssT",CME)

def fSSR(m,n):
    "model es una parte del  SS"
    global SSR
    a,b=modeloRLS(m,n)
    sxy=fsxy(m,n)
    SSR=b*sxy
    
    print("SSR=",SSR)
    return SSR

def fAnova(m,n):
    global MSE,Fc,S2
    SSE=fSSE(m, n)
    SSR=fSSR(m, n)#
    SST=fSS(m, n)
    MSE=SSR/1
    S2=SSE/(n-2)
    Fc=MSE/S2
    #div=SSR/S2
    print("Anova=",SSE, SST,SSR,MSE,S2,Fc)
    return SST,SSE,SSR,MSE,S2,Fc

def fScuad(m,n):
    sxx=fsxx(m,n)
    syy=fsyy(m, n)
    sxy=fsxy(m, n)
    print ("Scuad",sxx,syy,sxy)
    return sxx,syy,sxy

def fErEp(m,n):
    CME=fCME(m, n)
    sxx=fsxx(m, n)
    ErEp=np.sqrt(CME/sxx)
    print("ErEp",(round(ErEp,3)))
        
def fEstp(m,n):
    "Estadístico prueba para la pendiente"
    CME=fCME(m, n)
    sxx=fsxx(m, n)
    a,b=modeloRLS(m,n)
    Estp=b/math.sqrt(CME/sxx)
    print("Estp=",(round(Estp  ,3)))
      
def fErEi(m,n):
    "Error estandar de estimacion para la intersección"
    CME=fCME(m, n)
    sxx=fsxx(m, n)
    px,py=fprom(m,n)
    ErEi=math.sqrt(CME*((1/n)+(px**2/sxx)))
    #print"ErEp",ErEp
    print ("ErEi=",(round(ErEi,3)))
    
def fDistt(n):#c nivel de significancia
    global T
    df=n-2
    T=t.ppf(0.05,df)#ppf devuelve la probabilidad dado el 
    print ("t=",T)
    return T,df

def fIntConf(m,n):#intervalo de confinaza para la pendiente.
    global vexaa,vey,veyz,veyzz
    
    #T,df=fDistt(n)
    CME=fCME(m, n)
    sxx=fsxx(m, n)
    px,py,svy,svyc=fprom(m,n)
    vx, vxt=fvx(m)
    vy, vyt=fvy(m)
    
    ErEiYX0 = [math.sqrt(CME*((1/n)+(i-px)**2/sxx)) for (i) in zip(vx)]
    ErEiYX=np.array(ErEiYX0,np.float)
    
    ya=np.array([(i-j) for (i,j) in zip(vy,ErEiYX0)])
    yz=np.array([(i+j) for (i,j) in zip(vy,ErEiYX0)])
    vex= [num for elem in vx for num in elem]
    vey= [num for elem in vy for num in elem]
    veyz= [num for elem in yz for num in elem]
    veyzz= [round(num,2) for elem in veyz for num in elem]
    vexa= [num for elem in ya for num in elem]
    vexaa= [round(num,2) for elem in vexa for num in elem]
    """ print "vexaz=",veyzz
    print "vy=",vey
    print "vexaa=",vexaa """
    return veyzz,vey,vexaa


def fVarianzaDesvEstandar(m,n):
    global var,desv
    
    py,svy,svy,svyc=fprom(m,n)
    vx, vxt=fvx(m)
    vy, vyt=fvy(m)
    va=np.array([(i-py)**2 for (i) in zip(vy)])
    vari=np.array(va,np.float)
    varia=vari.sum()
    var=varia/(n-1)
    desv=math.sqrt(var)
    return var,desv
    
    print ("py=",py)
    print ("y=",vy)
    print("varianza=",var)
    print("desv=",desv)
    
    
    
def fIntConfG(m,n):
    "Error estandar de estimacion Y|X0 "
    global vex,vexa,vexaa,vey,veyz,veyzz
    
    T,df=fDistt(n)
    CME=fCME(m, n)
    sxx=fsxx(m, n)
    py,svy,svy,svyc=fprom(m,n)
    vx, vxt=fvx(m)
    vy, vyt=fvy(m)
    ErEiYX0 = [math.sqrt(CME*((1/n)+(i-px)**2/sxx)) for (i) in zip(vx)]
    ErEiYX=np.array(ErEiYX0,np.float)
    
    ya=np.array([(i-j) for (i,j) in zip(vy,ErEiYX0)])
    yz=np.array([(i+j) for (i,j) in zip(vy,ErEiYX0)])
    
    vex= [num for elem in vx for num in elem]
    vey= [num for elem in vy for num in elem]
    
    veyz= [num for elem in yz for num in elem]
    veyzz= [num for elem in veyz for num in elem]
    
    
    vexa= [num for elem in ya for num in elem]
    vexaa= [num for elem in vexa for num in elem]
    

    grafico.plot(vex,vey)
    grafico.scatter(vex,vey)
    grafico.scatter(vex,veyzz)
    grafico.plot(vex,veyzz)
    grafico.scatter(vex,vexaa)
    grafico.plot(vex,vexaa)
    grafico.show()
    return vex,vexa,vexaa,vey,veyz,veyzz
          
def fEsti(m,n):   
    CME=fCME(m, n)
    sxx=fsxx(m, n)
    px,py=fprom(m, n)
    a,b=modeloRLS(m, n)
    Esti=b/(math.sqrt(CME*((1/n)+(px**2/sxx))))
    print("Esti=",Esti)
        
def fDistnorm():
    global z
    w = float(input("Digite:")) #ingresas un valor por teclado
    # (w/100.0) calcula el prorentaja y (((1.0-(w/100.0)))) la cola inferiror
    # dado un porcentaje N%/100 y a esto sumarle la cola inferior
    val=(w/100.0)+(((1.0-(w/100.0))))/2
    z=norm.ppf(val)
    print ("val=",val)
    print ("z=",round(z,3))
    return  z

def fEstPrue(m,n):
    "Estadistico de prueba para tb0"
    global tbo
    T,df=fDistt(n)
    a,b=modeloRLS(m,n)
    r,rc,ra=fr(m,n)
    CME=fCME(m,n)
    sxx=fsxx(m,n)
    tbo=b/mtah.sqrt(CME/sxx)
    print("Est adistico de prueba b0=", tbo)
    if abs(tbo)>abs(T):
        print("Como estadistico prueba para b0=",tbo,"mayor que ",abs(T),"No se rechasa H0")
    else:
        print("S rechasa H0=")
    return tbo

def fIntConfP():
    global intif,intsu
    z=fDistnorm()
    py,svy,svy,svyc=fprom(m,n)
    var,desv=fVarianzaDesvEstandar(m,n)
    intif=py-z*desv/math.sqrt(n)
    intsu=py+z*desv/math.sqrt(n)
    print("n=",n)
    print ("py=",py)
    print("svy=",svy)
    print("desv=",desv)
    print("intif=",round(intif,1))
    print("intsu=",round(intsu,1))
    return intif,intsu
m,n,data=leerArchivo() 

fprom(m,n)
"""

fvy(m)
fvx(m)
modeloRLS(m,n)
vectorxy(m)

fr(m,n)
fSS(m,n)
fSSTx(m,n)
fIntConfG(m,n)
fprom(m,n)
"""