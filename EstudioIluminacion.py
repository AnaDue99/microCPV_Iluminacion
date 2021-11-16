# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 21:00:45 2021

@author: Ana Dueñas
"""
import function as f
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Leemos los datos del CSV para los 12 AOI distintos
deg0,deg5, deg10,deg15,deg20,deg25,deg30,deg35,deg40,deg45,deg50,deg55,deg60 = f.read_aoi_data()	


aoi_distribution=f.area_spot(11)


f.plot_aoi_data(deg10)
f.plot_aoi_data(deg15)
f.plot_aoi_data(aoi_distribution)

deg50=f.calcular_area(deg50)            
            

#plt.plot(perimetro_[0],perimetro_[1])
f.plot_aoi_data(deg50)           
area=np.empty(501, 501)   #COMPROBAR ESTO COMO SE HACE

#han de ser valores como con mucho 0,04 mm de precision 
posx=-0.04
posy=0.08
l1=0.36
l2=0.32
if posx<0:
        x=250-posx/20*500
else:
    x=250+posx/20*500 
if posy<0:
    y=250-posy/20*500
else:
    y=250+posy/20*500 
l1=l1/20*500
l2=l2/20*500    

for i in range(0,500,1):
    for j in range(0,500,1):
        area[i,j]=0
        
for i in range(round(-l1/2),round(l1/2),1):
    for j in range(round(-l2/2),round(l2/2),1):
        area[i+posx,j+posy]=1
        
        
            
    


    
