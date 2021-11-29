# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
import numpy as np

########################## FUNCIONES PRINCIPALES UTILIZADAS EN EL CODIGO##############

                        ##DEFINICIÓN CELCULA RECTANGULAR##
def rectangular_cell(l1,l2,desx,desy,precision=0.04):
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

                        ##DEFINICIÓN CELCULA CIRCULAR##
def circular_cell(r,desx,desy,precision=0.04):
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

  ##!!!!!!!!!! INTERSECCIÓN ÁREAS->Devuelve grid iluminación y electricidad##
def areas_intersection(area_spot,area_celula):
    area_iluminacion=np.empty((501, 501),float)
    area_electricidad=np.empty((501, 501),float)
    
    for i in range(len(area_spot[0])):
        for j in range(len(area_spot[0])):
            if area_spot[i,j]>0 and area_celula[i,j]==1:  
                area_electricidad[i,j]=area_spot[i,j]
            elif area_spot[i,j]>0 and area_celula[i,j]==0:
                area_iluminacion[i,j]=area_spot[i,j]
    
    
    return area_iluminacion, area_electricidad

