# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:42:49 2021

@author: anadu
"""
#Librerías utilizadas en el modulo:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pvlib import location
from pvlib import irradiance


#Tamaño grid reducido del spot. 
sizex=356
sizey=356

########################## FUNCIONES PRINCIPAL UTILIZADA EN EL CODIGO##############

                        ### OBTENER GRID DE UN SPOT##
## Función devuelve grid del spot para un aoi en concreto. Si no se conoce el grid
## del aoi en concreto, se llama a una función que interpola entre los dos grids conocidos
def spot_grid(aoi):
    cte=1/0.00028 #Constante para conseguir entrada a la celula de 1000W/m2
                  
    if aoi <5:
        if aoi==0:
            aoi_distribution=read_csv(0)
        else:
            aoi_distribution=generic_spot_grid(aoi,0,5,read_csv(0),read_csv(5))
    elif aoi<10:
        if aoi==5:
            aoi_distribution=read_csv(5)
        else:
            aoi_distribution=generic_spot_grid(aoi,5,10,read_csv(5),read_csv(10))
    elif aoi<15:
        if aoi==10:
            aoi_distribution=read_csv(10)
        else:
            aoi_distribution=generic_spot_grid(aoi,10,15,read_csv(10),read_csv(15))
    elif aoi<20:
        if aoi==15:
            aoi_distribution=read_csv(15)
        else:
            aoi_distribution=generic_spot_grid(aoi,15,20,read_csv(15),read_csv(20))
    elif aoi<25:
        if aoi==20:
            aoi_distribution=read_csv(20)
        else:
            aoi_distribution=generic_spot_grid(aoi,20,25,read_csv(20),read_csv(25))
    elif aoi<30:
        if aoi==25:
            aoi_distribution=read_csv(25)
        else:
            aoi_distribution=generic_spot_grid(aoi,25,30,read_csv(25),read_csv(30))
    elif aoi<35:
        if aoi==30:
            aoi_distribution=read_csv(30)
        else:
            aoi_distribution=generic_spot_grid(aoi,30,35,read_csv(30),read_csv(35))
    elif aoi<40:
        if aoi==35:
            aoi_distribution=read_csv(35)
        else:
            aoi_distribution=generic_spot_grid(aoi,35,40,read_csv(35),read_csv(40))
    elif aoi<45:
        if aoi==40:
            aoi_distribution=read_csv(40)
        else:
            aoi_distribution=generic_spot_grid(aoi,40,45,read_csv(40),read_csv(45))
    elif aoi<50:
        if aoi==45:
            aoi_distribution=read_csv(45)
        else:
            aoi_distribution=generic_spot_grid(aoi,45,50,read_csv(45),read_csv(50))
    elif aoi<55:
        if aoi==50:
            aoi_distribution=read_csv(50)
        else:
            aoi_distribution=generic_spot_grid(aoi,50,55,read_csv(50),read_csv(55))
    elif aoi<60:
        if aoi==55:
            aoi_distribution=read_csv(55)
        else:
            aoi_distribution=generic_spot_grid(aoi,55,60,read_csv(55),read_csv(60))
    elif aoi==60:
        aoi_distribution=read_csv(60)
        
    else:
       aoi_distribution=np.zeros((sizex, sizey),float)
    

    return aoi_distribution*cte

                               ### DIBUJAR SPOT##
#Función para dibujar como heatmap el grid de un aoi con título.
def plot_grid(title,aoi_distribution):
    #Resolucion es de 0.04 mm   
    with sns.axes_style("white"):
        sns.heatmap(aoi_distribution,vmin=0,  vmax=6, square=True,  cmap="YlGnBu_r")
        plt.title(title)
        plt.show()
       
                 ###DATOS IRRADIANCIA LOCALIACIÓN##
#Función que recoge varias funciones de la libreria pvlib para conocer caracteristicas
#de irradiancia del emplazamiento elegido basado en unas características

def get_data_location(caracteristics,caracteristics_module,date):
    site = location.Location(caracteristics['lat'], 
                             caracteristics['lon'],
                            caracteristics['tz'])                                                      
    times = pd.date_range(date, freq='10min', periods=6*24,
                      tz=site.tz)
    clearsky = site.get_clearsky(times)
    solar_position = site.get_solarposition(times)
    
    total_irrad=irradiance.get_total_irradiance( 
    surface_tilt=caracteristics_module['tilt'],
    surface_azimuth=caracteristics_module['surface_azimuth'],
    dni=clearsky['dni'],
    ghi=clearsky['ghi'],
    dhi=clearsky['dhi'],
    solar_zenith=solar_position['apparent_zenith'],
    solar_azimuth=solar_position['azimuth'])
    
    AOI_=irradiance.aoi( caracteristics_module['tilt'],
                   caracteristics_module['surface_azimuth'],
                   solar_position['apparent_zenith'], 
                   solar_position['azimuth'])
    
    AOI= AOI_ 
    for i in range(len(AOI_)):
        if AOI_[i]>90:
            AOI[i]=90
        else:
            AOI[i]=AOI_[i]
    
    AOI.index = AOI.index.strftime("%H:%M")
    total_irrad.index = total_irrad.index.strftime("%H:%M")
    return pd.DataFrame({'AOI': AOI,
                         'POA_direct': total_irrad['poa_direct'],
                         'POA_diffuse': total_irrad['poa_diffuse'],
                         'POA_tot':total_irrad['poa_global'],
                         'times':times})

#################### FUNCIONES UTILIZADAS EN LAS FUNCIONES ANTERIORES #################                                

                                #### LECTURA CSV ###
def read_csv(aoi):
    #Leemos del CSV los datos
   path = f"spots inso 29-Oct-2021\InsoPMMA_{aoi}deg\OptiMesh_{aoi}deg.csv"
   Deg = pd.read_csv(path, index_col=0)
   deg=Deg.to_numpy()
   spot=reduce_(deg)
      
   return spot

                                
                            ###FUNCION CALCULA LA MATRIZ INTERPOLANDO ###
def generic_spot_grid(x,xa,xb,aoi1,aoi2):     
    p1=aoi_half_point(aoi1)   
    p2=aoi_half_point(aoi2)                     
    p3=linear_interpolation(x, xa, xb, p1, p2)
    
    ##Creamos la matriz interpolada:
    desp1=p3-p1
    desp2=p3-p2
    
    aoi3=np.zeros((sizex, sizey),float)
    aoi4=np.zeros((sizex, sizey),float)
    for i in range(len(aoi3[0])):
        for j in range(len(aoi3[0])):
            
            desp1_0=int(i-desp1[0])
            desp1_1=int(j-desp1[1])
            desp2_0=int(i-desp2[0])
            desp2_1=int(j-desp2[1])
           
            if desp1_0 < sizex and desp1_1 < sizey and desp1_0 > 0 and desp1_1 > 0: 
                aoi3[i,j]+=aoi1[desp1_0,desp1_1]
           
            if  desp2_0 < sizex and desp2_1 < sizey  and desp2_0 > 0 and desp2_1 > 0:
                aoi4[i,j]+=aoi2[desp2_0,desp2_1]

    aoi_pedido=linear_interpolation(x, xa, xb, aoi3, aoi4)
    return aoi_pedido

                            ###REDUCIMOS EL TAMAÑO DEL GRID ###
def reduce_(aoi):
    aoi_reduce=np.zeros((sizex, sizey),float)
    restx=(501-sizex)/2
    resty=(501-sizey)/2
    for i in range(int(restx),int(501-restx),1):
        for j in range(int(resty),int(501-resty),1):
            aoi_reduce[int(i-restx),int(j-resty)]=aoi[i,j]
    return aoi_reduce

                          ####CALCULO PUNTO MAXIMA IRRADIANCIA AOI ##
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


