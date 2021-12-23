# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
import numpy as np
import module_AoiGrids as gr
sizex=251
sizey=251
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
            area[int(i+x),int(j+y)]=1
    return area

                        ##DEFINICIÓN CELCULA CIRCULAR##
def circular_cell(r,desy,desx,precision=0.04):
    area=np.zeros((sizex, sizey),int)
    #han de ser valores como con mucho 0,04 mm de precision 
    r=r/precision
    
    x=desx/precision
    y=desy/precision 
    
    for i in range(len(area[0])):
        for j in range(len(area[0])):
            if i**2+j**2 <= r**2 :
                area[int(i+x+sizex/2),int(j+y+sizey/2)]=1
                area[int(-i+x+sizex/2),int(j+y+sizey/2)]=1
                area[int(i+x+sizex/2),int(-j+y+sizey/2)]=1
                area[int(-i+x+sizex/2),int(-j+y+sizey/2)]=1
    return area

  ##!!!!!!!!!! INTERSECCIÓN ÁREAS->Devuelve grid iluminación y electricidad##
def areas_intersection(area_spot,area_celula):
    area_iluminacion=np.zeros((sizex, sizey),float)
    area_electricidad=np.empty((sizex, sizey),float)
    
    for i in range(len(area_spot[0])):
        for j in range(len(area_spot[0])):
            if area_spot[i,j]>0 and area_celula[i,j]==1:  
                area_electricidad[i,j]=area_spot[i,j]
            elif area_spot[i,j]>0 and area_celula[i,j]==0:
                area_iluminacion[i,j]=area_spot[i,j]
    
    
    return area_iluminacion, area_electricidad

def irradiance_cell(radio,dy,dx,AOI,directa,difusa):
    cell_grid=circular_cell(radio, dy, dx)
    spot=gr.spot_grid(AOI)
    area_illum,area_elect=areas_intersection(spot,cell_grid)
    irradiance=area_illum.sum()*directa+difusa
    return irradiance