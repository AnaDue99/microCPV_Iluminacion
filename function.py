# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
        
def plot_aoi_data(aoi_distribution):
    #Resolucion es de 0.04 mm   
    with sns.axes_style("white"):
        sns.heatmap(aoi_distribution,vmin=0,  vmax=0.00004, square=True,  cmap="YlGnBu_r")
        plt.show()   
   
def calcular_area(deg): #ESTO REALMENTE PARA QUE SIRVE ????? PARA NADA??? NO? PARA APROXIMAR??? PA QUE APROXIMAS???
    for i in range(len(deg[0])):
        for j in range(len(deg[0])):
            if deg[i,j]>0.00004:  #A LO MEJOR QUITAR ESTO
                deg[i,j]=1
                
            elif deg[i,j]<0.00004: #Y DEJAR ESTO PARA NO TENER PROBLEMAS??? 
                deg[i,j]=0
    return deg


                