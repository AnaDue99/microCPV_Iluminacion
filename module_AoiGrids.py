# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:42:49 2021

@author: anadu
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

########################## FUNCIONES PRINCIPAL UTILIZADA EN EL CODIGO##############
def spot_grid(aoi):
    Deg0,Deg5, Deg10,Deg15,Deg20,Deg25,Deg30,Deg35,Deg40,Deg45,Deg50,Deg55,Deg60 = read_csv()
    
    
    if aoi<0:
        NEGATIVO=1    
        aoi=-aoi
    else:
        NEGATIVO=0
                
    if aoi <5:
        if aoi==0:
            aoi_distribution=Deg0
        else:
            aoi_distribution=generic_spot_grid(aoi,0,5,Deg0,Deg5)
    elif aoi<10:
        if aoi==5:
            aoi_distribution=Deg5
        else:
            aoi_distribution=generic_spot_grid(aoi,5,10,Deg5,Deg10)
    elif aoi<15:
        if aoi==10:
            aoi_distribution=Deg10
        else:
            aoi_distribution=generic_spot_grid(aoi,10,15,Deg10,Deg15)
    elif aoi<20:
        if aoi==15:
            aoi_distribution=Deg15
        else:
            aoi_distribution=generic_spot_grid(aoi,15,20,Deg15,Deg20)
    elif aoi<25:
        if aoi==20:
            aoi_distribution=Deg20
        else:
            aoi_distribution=generic_spot_grid(aoi,20,25,Deg20,Deg25)
    elif aoi<30:
        if aoi==25:
            aoi_distribution=Deg25
        else:
            aoi_distribution=generic_spot_grid(aoi,25,30,Deg25,Deg30)
    elif aoi<35:
        if aoi==30:
            aoi_distribution=Deg30
        else:
            aoi_distribution=generic_spot_grid(aoi,30,35,Deg30,Deg35)
    elif aoi<40:
        if aoi==35:
            aoi_distribution=Deg35
        else:
            aoi_distribution=generic_spot_grid(aoi,35,40,Deg35,Deg40)
    elif aoi<45:
        if aoi==40:
            aoi_distribution=Deg40
        else:
            aoi_distribution=generic_spot_grid(aoi,40,45,Deg40,Deg45)
    elif aoi<50:
        if aoi==45:
            aoi_distribution=Deg45
        else:
            aoi_distribution=generic_spot_grid(aoi,45,50,Deg45,Deg50)
    elif aoi<55:
        if aoi==50:
            aoi_distribution=Deg50
        else:
            aoi_distribution=generic_spot_grid(aoi,50,55,Deg50,Deg55)
    elif aoi<60:
        if aoi==55:
            aoi_distribution=Deg55
        else:
            aoi_distribution=generic_spot_grid(aoi,55,60,Deg55,Deg60)
    elif aoi==60:
        aoi_distribution=Deg60
        
    else:
        print("AOI FUERA DE ESTUDIO")
        aoi_distribution=np.empty((501, 501),float)
    
    if NEGATIVO==1:
        aoi_distribution=mirror_grid(aoi_distribution)
    return aoi_distribution

def plot_grid(aoi,aoi_distribution):
    #Resolucion es de 0.04 mm   
    with sns.axes_style("white"):
        sns.heatmap(aoi_distribution,vmin=0,  vmax=0.00004, square=True,  cmap="YlGnBu_r")
        plt.title(aoi)
        plt.show()
        
def mirror_grid(aoi):
    aoi_mirror=np.empty((501, 501),float)
    for i in range(len(aoi[0])):
        for j in range(len(aoi[0])):
            aoi_mirror[i,j]=aoi[i,500-j]
    return aoi_mirror

def transform_aoi(AOI):
    for x in range(len(AOI)):
        if AOI[x]>90:
            AOI[x]=90
            
    min_AOI=min(AOI)
    for x in range(len(AOI)):
        if AOI[x]==min_AOI:
            a=x
            for x in range(a,len(AOI)):
              AOI[x]=-AOI[x]
    
    for x in range(len(AOI)):
        if AOI[x]>90:
            AOI[x]=90
        return AOI
#################### FUNCIONES UTILIZADAS EN LAS FUNCIONES ANTERIORES #################                                

                                #### LECTURA CVS ###
def read_csv():
    #Leemos del CSV los datos
    Deg0 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_0deg\OptiMesh_0deg.csv")   
    Deg5 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_5deg\OptiMesh_5deg.csv") 
    Deg10 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_10deg\OptiMesh_10deg.csv")   
    Deg15 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_15deg\OptiMesh_15deg.csv") 
    Deg20 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_20deg\OptiMesh_20deg.csv")   
    Deg25 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_25deg\OptiMesh_25deg.csv") 
    Deg30 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_30deg\OptiMesh_30deg.csv")   
    Deg35 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_35deg\OptiMesh_35deg.csv") 
    Deg40 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_40deg\OptiMesh_40deg.csv")   
    Deg45 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_45deg\OptiMesh_45deg.csv") 
    Deg50 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_50deg\OptiMesh_50deg.csv")   
    Deg55 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_55deg\OptiMesh_55deg.csv") 
    Deg60 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_60deg\OptiMesh_60deg.csv")
    
    #Pasamos la columna NaN a indice. 
    
    Deg5.set_index('NaN',inplace=True)
    Deg10.set_index('NaN',inplace=True)
    Deg15.set_index('NaN',inplace=True)
    Deg20.set_index('NaN',inplace=True)
    Deg25.set_index('NaN',inplace=True)
    Deg30.set_index('NaN',inplace=True)
    Deg35.set_index('NaN',inplace=True)
    Deg40.set_index('NaN',inplace=True)
    Deg45.set_index('NaN',inplace=True)
    Deg50.set_index('NaN',inplace=True)
    Deg55.set_index('NaN',inplace=True)
    Deg60.set_index('NaN',inplace=True)
   
    #Se ha preferido trabajar con matrices aunque no descarto intentarlo con dataframe luego
    deg0=Deg0.to_numpy()
    deg5=Deg5.to_numpy()
    deg10=Deg10.to_numpy()
    deg15=Deg15.to_numpy()
    deg20=Deg20.to_numpy()
    deg25=Deg25.to_numpy()
    deg30=Deg30.to_numpy()
    deg35=Deg35.to_numpy()
    deg40=Deg40.to_numpy()
    deg45=Deg45.to_numpy()
    deg50=Deg50.to_numpy()
    deg55=Deg55.to_numpy()
    deg60=Deg60.to_numpy()
    
    return  deg0, deg5,deg10, deg15,deg20,deg25,deg30,deg35,deg40,deg45,deg50,deg55,deg60
                                
                            ###FUNCION CALCULA LA MATRIZ ###
def generic_spot_grid(x,xa,xb,aoi1,aoi2): 
    
    p1=aoi_half_point(aoi1)   
    p2=aoi_half_point(aoi2)  
                   
    p3=linear_interpolation(x, xa, xb, p1, p2)
    
    ##Creamos la matriz interpolada:
    desp1=p3-p1
    desp2=p3-p2
    
    aoi3=np.empty((501, 501),float)
    aoi4=np.empty((501, 501),float)
    for i in range(len(aoi3[0])):
        for j in range(len(aoi3[0])):
            
            desp1_0=int(i-desp1[0])
            desp1_1=int(j-desp1[1])
            desp2_0=int(i-desp2[0])
            desp2_1=int(j-desp2[1])
           
            if desp1_0 < 501 and desp1_1 < 501 and desp1_0 > 0 and desp1_1 > 0: 
                aoi3[i,j]+=aoi1[desp1_0,desp1_1]
           
            if  desp2_0 < 501 and desp2_1 < 501  and desp2_0 > 0 and desp2_1 > 0:
                aoi4[i,j]+=aoi2[desp2_0,desp2_1]

    aoi_pedido=linear_interpolation(x, xa, xb, aoi3, aoi4)
    return aoi_pedido

                          ####CALCULO PUNTO MAXIMO AOI ##
def aoi_half_point(aoi):
    max_=0
    for i in range(len(aoi[0])):
        for j in range(len(aoi[0])):
            if aoi[i,j]>max_:
                max_=aoi[i,j]
                p=np.array([i,j])
    
    #Ver si hay mas puntos muy altos: registrar 1
    for i in range(len(aoi[0])):
        for j in range(len(aoi[0])):
            if aoi[i,j]>max_*0.99:
                p_=np.array([i,j])
                p=(p+p_)/2
    return p
                                    ###INTERPOLACIÓN LINEAL ####
def linear_interpolation(x,xa,xb,ya,yb):
    #x: valor AOI requiero, xa y xb valore que se tienen. 
    #ya yb son las matrices de los aoi que se tienen
    y=ya+(x-xa)*(yb-ya)/(xb-xa)
    return y 

