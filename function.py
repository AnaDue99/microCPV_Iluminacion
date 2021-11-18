# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def read_aoi_data():
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
    Deg0.set_index('NaN',inplace=True)
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

#Interpolación lineal-> no funciona tengo que encontrar otro método
def linear_interpolation(x,xa,xb,ya,yb):
    y=ya+(x-xa)*(yb-ya)/(xb-xa)
    return y                        

 
def area_spot(aoi):
    Deg0,Deg5, Deg10,Deg15,Deg20,Deg25,Deg30,Deg35,Deg40,Deg45,Deg50,Deg55,Deg60 = read_aoi_data()
    if aoi>0 and aoi <5:
        aoi_distribution=linear_interpolation(aoi,0,5,Deg0,Deg5)
    elif aoi<10:
        aoi_distribution=linear_interpolation(aoi,5,10,Deg5,Deg10)
    elif aoi<15:
        aoi_distribution=linear_interpolation(aoi,10,15,Deg10,Deg15)
    elif aoi<20:
        aoi_distribution=linear_interpolation(aoi,15,20,Deg15,Deg20)
    elif aoi<25:
        aoi_distribution=linear_interpolation(aoi,20,25,Deg20,Deg25)
    elif aoi<30:
        aoi_distribution=linear_interpolation(aoi,25,30,Deg25,Deg30)
    elif aoi<35:
        aoi_distribution=linear_interpolation(aoi,30,35,Deg30,Deg35)
    elif aoi<40:
        aoi_distribution=linear_interpolation(aoi,35,40,Deg35,Deg40)
    elif aoi<45:
        aoi_distribution=linear_interpolation(aoi,40,45,Deg40,Deg45)
    elif aoi<50:
        aoi_distribution=linear_interpolation(aoi,45,50,Deg45,Deg50)
    elif aoi<55:
        aoi_distribution=linear_interpolation(aoi,50,55,Deg50,Deg55)
    elif aoi<60:
        aoi_distribution=linear_interpolation(aoi,55,60,Deg55,Deg60)
    else:
        print("AOI FUERA DE ESTUDIO")
    
 

    return aoi_distribution
        
def plot_data_grid(aoi_distribution):
    #Resolucion es de 0.04 mm   
    with sns.axes_style("white"):
        sns.heatmap(aoi_distribution,vmin=0,  vmax=0.00004, square=True,  cmap="YlGnBu_r")
        plt.show()   
   


#INTENTAR HACER UNA FUNCION TANTO PARA RECTANGULAR COMO PARA CIRCULAR
def definir_area_celula_rectanular(l1,l2,desx,desy,precision=0.04):
    area=np.empty((501, 501),float)
    #han de ser valores como con mucho 0,04 mm de precision 
    l1=l1/precision
    l2=l2/precision
    if desx<0:
        x=desx/precision
    else:
        x=desx/precision 
    if desy<0:
        y=-desy/precision
    else:
        y=desy/precision 
    for i in range(round(250-l1/2),round(250+l1/2),1):
        for j in range(round(250-l2/2),round(250+l2/2),1):
            area[int(i+x),int(j+y)]=1
    return area

def definir_area_celula_circular(r,desx,desy,precision=0.04):#Lo he aproximado a un cuadrado no me gusta
    area=np.empty((501, 501),float)
    #han de ser valores como con mucho 0,04 mm de precision 
    r=r/precision
    
    if desx<0:
        x=desx/precision
    else:
        x=desx/precision 
    if desy<0:
        y=-desy/precision
    else:
        y=desy/precision 
    
    for i in range(len(area[0])):
        for j in range(len(area[0])):
            if i**2+j**2 <= r**2 :
                area[int(i+x+250),int(j+y+250)]=1
                area[int(-i+x+250),int(j+y+250)]=1
                area[int(i+x+250),int(-j+y+250)]=1
                area[int(-i+x+250),int(-j+y+250)]=1
    return area

def calculo_diferencia_areas(area_spot,area_celula):
    area_iluminacion=np.empty((501, 501),float)
    area_electricidad=np.empty((501, 501),float)
    
    for i in range(len(area_spot[0])):
        for j in range(len(area_spot[0])):
            if area_spot[i,j]>0 and area_celula[i,j]==1:  
                area_electricidad[i,j]=area_spot[i,j]
            elif area_spot[i,j]>0 and area_celula[i,j]==0:
                area_iluminacion[i,j]=area_spot[i,j]
    
    
    return area_iluminacion, area_electricidad



#ESTO REALMENTE PARA QUE SIRVE ????? PARA NADA??? NO? PARA APROXIMAR??? PA QUE APROXIMAS???
def calcular_area(deg): 
    for i in range(len(deg[0])):
        for j in range(len(deg[0])):
            if deg[i,j]>0.00004:  #A LO MEJOR QUITAR ESTO
                deg[i,j]=1
                
            elif deg[i,j]<0.00004: #Y DEJAR ESTO PARA NO TENER PROBLEMAS??? 
                deg[i,j]=0
    return deg