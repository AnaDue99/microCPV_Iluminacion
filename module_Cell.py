# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
#Librerías utilizadas en el modulo:

import numpy as np
import module_AoiGrids as gr
from scipy.interpolate import InterpolatedUnivariateSpline as interp
#Tamaño grid reducido del spot. 
sizex=356
sizey=356

########################## FUNCIONES PRINCIPALES UTILIZADAS EN EL CODIGO##############

                        ##DEFINICIÓN CELULA RECTANGULAR##
def rectangular_cell(l1,l2,desx,desy,precision=0.04):
    area=np.zeros((sizex, sizey),int)
    #han de ser valores como con mucho 0,04 mm de precision 
    l1=l1/precision
    l2=l2/precision
    x=desx/precision
    y=desy/precision
     
    for i in range(round(sizex/2-l1/2),round(sizex/2+l1/2),1):
        for j in range(round(sizey/2-l2/2),round(sizey/2+l2/2),1):
            area[int(i+x),int(j+y)]=10
    return area

                        ##DEFINICIÓN CELULA CIRCULAR##
def circular_cell(r,desx,desy,precision=0.04):
    area=np.zeros((sizex, sizey),int)
    #han de ser valores como con mucho 0,04 mm de precision 
    r=r/precision    
    x=desx/precision
    y=desy/precision 
    
    for i in range(len(area[0])):
        for j in range(len(area[0])):
            if i**2+j**2 <= r**2 :
                area[int(i+y+sizey/2),int(j+x+sizex/2)]=10
                area[int(-i+y+sizey/2),int(j+x+sizex/2)]=10
                area[int(i+y+sizey/2),int(-j+x+sizex/2)]=10
                area[int(-i+y+sizey/2),int(-j+x+sizex/2)]=10
    return area

 

 ###DEFINICIÓN FUNCIONES DE LA IRRADIANCIA DEPENDIENDO DEL AOI Y EL DESP ###
def function(desp,radio):
    irradiance_aoi_0=[]
    irradiance_aoi_5=[]
    irradiance_aoi_10=[]
    irradiance_aoi_15=[]
    irradiance_aoi_20=[]
    irradiance_aoi_25=[]
    irradiance_aoi_30=[]
    irradiance_aoi_35=[]
    irradiance_aoi_40=[]
    irradiance_aoi_45=[]
    irradiance_aoi_50=[]
    irradiance_aoi_55=[]
    irradiance_aoi_60=[]

    for i in desp:
        irradiance_aoi_0.append(irradiance_cell(radio, i, 0, 0))
        irradiance_aoi_5.append(irradiance_cell(radio, i, 0, 5))
        irradiance_aoi_10.append(irradiance_cell(radio, i, 0, 10))
        irradiance_aoi_15.append(irradiance_cell(radio, i, 0, 15))
        irradiance_aoi_20.append(irradiance_cell(radio, i, 0, 20))
        irradiance_aoi_25.append(irradiance_cell(radio, i, 0, 25))
        irradiance_aoi_30.append(irradiance_cell(radio, i, 0, 30))
        irradiance_aoi_35.append(irradiance_cell(radio, i, 0, 35))
        irradiance_aoi_40.append(irradiance_cell(radio, i, 0, 40))
        irradiance_aoi_45.append(irradiance_cell(radio, i, 0, 45))
        irradiance_aoi_50.append(irradiance_cell(radio, i, 0, 50))
        irradiance_aoi_55.append(irradiance_cell(radio, i, 0, 55))
        irradiance_aoi_60.append(irradiance_cell(radio, i, 0, 60))
        
    f_0=interp(desp,irradiance_aoi_0,k=3)
    f_5=interp(desp,irradiance_aoi_5,k=3)
    f_10=interp(desp+1.06,irradiance_aoi_10,k=3)
    f_15=interp(desp+1.26,irradiance_aoi_15,k=3)
    f_20=interp(desp+2.31,irradiance_aoi_20,k=3)
    f_25=interp(desp+2.76,irradiance_aoi_25,k=3)
    f_30=interp(desp+3.93,irradiance_aoi_30,k=3)
    f_35=interp(desp+4.79,irradiance_aoi_35,k=3)
    f_40=interp(desp+5.46,irradiance_aoi_40,k=3)
    f_45=interp(desp+7.06,irradiance_aoi_45,k=3)
    f_50=interp(desp+8.21,irradiance_aoi_50,k=3)
    f_55=interp(desp+8.86,irradiance_aoi_55,k=3)
    f_60=interp(desp+11.05,irradiance_aoi_60,k=3)
    
    return f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60
    

    #FUNCIÓN DE RENDIMIENTO PARA CADA CURVA ###
def performance_curve(desp,aoi,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60):    
    if aoi<2.5:
       irrad=f_0(desp)
        
    elif aoi<7.5:
        irrad=f_5(desp)
        
    elif aoi<12.5:
        irrad=f_10(desp)
        
    elif aoi<17.5:
        irrad=f_15(desp)
        
    elif aoi<22.5:
       irrad=f_20(desp)
       
    elif aoi<27.5:
        irrad=f_25(desp)
        
    elif aoi<32.5:
        irrad=f_30(desp)
       
    elif aoi<37.5:
        irrad=f_35(desp)
        
    elif aoi<42.5:
       irrad=f_40(desp)
       
    elif aoi<47.5:
        irrad=f_45(desp)
        
    elif aoi<52.5:
        irrad=f_50(desp)
        
    elif aoi<57.5:
        irrad=f_55(desp)
     
    elif aoi==60:
        irrad=f_60(desp)
    else: 
        irrad=0
    
    return irrad

### FUNCIÓN QUE DADO UN VALOR DE ILUMINACIÓN Y UN AOI, AJUSTA EL DESPLAZAMIENTO REQUERIDO PARA ELLO ###

def adjust(lum_cte,aoi,area,directa,difusa,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60):
    desp=-2
    rad_cte=from_lum_to_pot(lum_cte)
    val_rad=performance_curve(desp,aoi,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60)*directa+difusa*area #W
    
    
    while val_rad>rad_cte:
        desp=desp+0.01   
        val_rad=performance_curve(desp,aoi,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60)*directa+difusa*area
    
  
        
    illum_out=from_pot_to_lum(val_rad)
      
    return desp,illum_out



    ##### FUNCIONES PARA PASAR DE IRRADIANCIA A ILUMINACION Y VICEVERSA ####
def from_pot_to_lum(Pot_rad):
    #Pot_rad está en W
    #Area está en m2
    
    Lumen=Pot_rad*105 
    return Lumen

def from_rad_to_lum(Rad,area):
    Lumen=Rad*105*area
    return Lumen
    
def from_lum_to_pot(Lumen):
    #Area está en m2
    Pot_rad=Lumen/105 #W
    
    return Pot_rad #W



############# FUNCIONES UTILIZADAS EN LAS ANTERIORES #####################

           ### DEVUELVE VALOR IRRADIANCIA PARA ILUMINACIÓN ###
def irradiance_cell(radio,dy,dx,AOI):    
    area_elemento=0.16*10**-6
    cell_grid=circular_cell(radio, dy, dx)
    spot=gr.spot_grid(AOI)
    area_illum,area_elect=areas_intersection(spot,cell_grid)
    illum=area_illum.sum()*area_elemento
    elect=area_elect.sum()*area_elemento 
    return illum #En W se devuelve

        ## INTERSECCIÓN ÁREAS->Devuelve grid iluminación y electricidad##  
def areas_intersection(area_spot,area_celula):
    area_iluminacion=np.zeros((sizex, sizey),float)
    area_electricidad=np.zeros((sizex, sizey),float)
    
    for i in range(len(area_spot[0])):
        for j in range(len(area_spot[0])):
            if area_spot[i,j]>0 and area_celula[i,j]==10:  
                area_electricidad[i,j]=area_spot[i,j]
            elif area_spot[i,j]>0 and area_celula[i,j]==0:
                area_iluminacion[i,j]=area_spot[i,j]
    
    
    return area_iluminacion, area_electricidad
            
            