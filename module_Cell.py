# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
import pandas as pd
import numpy as np
import module_AoiGrids as gr
from scipy.interpolate import InterpolatedUnivariateSpline as interp

sizex=201
sizey=201
########################## FUNCIONES PRINCIPALES UTILIZADAS EN EL CODIGO##############

                        ##DEFINICIÓN CELCULA RECTANGULAR##
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

                        ##DEFINICIÓN CELCULA CIRCULAR##
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

  ##!!!!!!!!!! INTERSECCIÓN ÁREAS->Devuelve grid iluminación y electricidad##
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

def irradiance_cell(radio,dy,dx,AOI,directa=1,difusa=0):    
    cell_grid=circular_cell(radio, dy, dx)
    spot=gr.spot_grid(AOI)
    area_illum,area_elect=areas_intersection(spot,cell_grid)
    irradiance=area_illum.sum()*directa+difusa
    illumination=irradiance*683*179*10**-6  #En lux  683lum/W  1 lumen= 1 lux/m2
    return illumination

def  desp_function(radio,desp,aoi):
    irrad_aoi=[]
    for i in desp:
        irrad_aoi.append(irradiance_cell(radio, i, 0, aoi))
    return irrad_aoi

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
    f_10=interp(desp,irradiance_aoi_10,k=3)
    f_15=interp(desp,irradiance_aoi_15,k=3)
    f_20=interp(desp,irradiance_aoi_20,k=3)
    f_25=interp(desp,irradiance_aoi_25,k=3)
    f_30=interp(desp,irradiance_aoi_30,k=3)
    f_35=interp(desp,irradiance_aoi_35,k=3)
    f_40=interp(desp,irradiance_aoi_40,k=3)
    f_45=interp(desp,irradiance_aoi_45,k=3)
    f_50=interp(desp,irradiance_aoi_50,k=3)
    f_55=interp(desp,irradiance_aoi_55,k=3)
    f_60=interp(desp,irradiance_aoi_60,k=3)
    
    return f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60
    
def irrad_BORRAR(desp,aoi,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60):    
    if aoi<5:
        if aoi==0:
            irrad=f_0(desp)
        else:
            irrad=gr.linear_interpolation(aoi,0,5,f_0(desp),f_5(desp))
    elif aoi<10:
        if aoi==5:
            irrad=f_5(desp)
        else:
            irrad=gr.linear_interpolation(aoi,5,10,f_5(desp),f_10(desp))
    elif aoi<15:
        if aoi==10:
            irrad=f_10(desp)
        else:
            irrad=gr.linear_interpolation(aoi,10,15,f_10(desp),f_15(desp))
    elif aoi<20:
        if aoi==15:
            irrad=f_15(desp)
        else:
            irrad=gr.linear_interpolation(aoi,15,20,f_15(desp),f_20(desp))
    elif aoi<25:
        if aoi==20:
            irrad=f_20(desp)
        else:
            irrad=gr.linear_interpolation(aoi,20,25,f_20(desp),f_25(desp))
    elif aoi<30:
        if aoi==25:
            irrad=f_25(desp)
        else:
            irrad=gr.linear_interpolation(aoi,25,30,f_25(desp),f_30(desp))
    elif aoi<35:
        if aoi==30:
            irrad=f_30(desp)
        else:
            irrad=gr.linear_interpolation(aoi,30,35,f_30(desp),f_35(desp))
    elif aoi<40:
        if aoi==35:
            irrad=f_35(desp)
        else:
            irrad=gr.linear_interpolation(aoi,35,40,f_35(desp),f_40(desp))
    elif aoi<45:
        if aoi==40:
            irrad=f_40(desp)
        else:
            irrad=gr.linear_interpolation(aoi,40,45,f_40(desp),f_45(desp))
    elif aoi<50:
        if aoi==45:
            irrad=f_45(desp)
        else:
            irrad=gr.linear_interpolation(aoi,45,50,f_45(desp),f_50(desp))
    elif aoi<55:
        if aoi==50:
            irrad=f_50(desp)
        else:
            irrad=gr.linear_interpolation(aoi,50,55,f_50(desp),f_55(desp))
    elif aoi<60:
        if aoi==55:
            irrad=f_55(desp)
        else:
            irrad=gr.linear_interpolation(aoi,55,60,f_55(desp),f_60(desp))
    elif aoi==60:
        irrad=f_60(desp)
    else: 
        irrad=0
    
    return irrad

def irrad(desp,aoi,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60):    
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
def from_irrad_to_ilum(irrad,area):
    #Irrad está en W/m2
    #Area está en m2
    Potencia_rad=irrad*area # W
    Potencia_lum=Potencia_rad*683 #Lux
    ilum=irrad*683  #Lumen
    return Potencia_lum

def from_ilum_to_irrad(Potencia_lum,area):
    #Potencia_lum en lux
    #Area está en m2
    Potencia_rad=Potencia_lum/683
    irrad=Potencia_rad/area      #W/m2
    return irrad


def adjust(illum_cte,aoi,area,directa,difusa,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60):
    desp=0 
    irrad_cte=from_ilum_to_irrad(illum_cte,area)
    val_irrad=irrad(desp,aoi,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60)*directa+difusa
       
    while val_irrad>irrad_cte:
        desp=desp+0.01
       
        val_irrad=irrad(desp,aoi,f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60)*directa+difusa
        
    illum_out=from_irrad_to_ilum(val_irrad,area)
        
    return desp,illum_out