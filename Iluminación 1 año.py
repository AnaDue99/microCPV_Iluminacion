# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 22:36:23 2021

@author: anadu

TRABAJAMOS CON TODO UN AÑO 
"""

import module_Cell as cell
import module_AoiGrids as gr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


## CREAMOS EL VECTOR DATE, CON COTODOS LOS DIAS DEL AÑO)
import numpy as np
date=np.array('2021-01-01', dtype=np.datetime64)
date= date + np.arange(365)


caracteristics_module={    
    'tilt':0,
    'surface_azimuth':180,
    'radius':1.2
    }

caracteristics={
    'lat':40.405655,
    'lon':-3.647649,
    'tz':'Etc/GMT-2',
    }
#COGEMOS LOS DATOS OBTENIDOS OPTIMOS PARA MANTENER UNA IRRADIANCIA DE 250 cte para 
#Solsticio de verano
vector_obtenido=[0.8, 0.8,   0.84 , 0.88 , 1.12 , 1.28 , 1.44 , 1.24 , 1.08 ,
                 0.92 , 0.8 ,  0.84 , 0.84 , 0.84 , 0.84, -0.86 ,-0.86 ,-0.86 ,
                 -0.86 ,-0.82 ,-0.9  ,-1.06, -1.22, -1.38 ,-1.34, -1.18 ,-0.94,
                 -0.9 , -0.86 ,-0.78 ,-0.78 ]
desp=np.zeros(144,float)

for i in range (71,102):
    desp[i]=vector_obtenido[i-71]
        
   
#Pasamos a probar con el solsticio de invernio y equinoccios. 

for day in range(len(date)):
    if day==46 or day==105 or day==166 or day==227 or day==288 or day==349:
        data_location=gr.get_data_location(caracteristics,caracteristics_module,date[day]) 
        print(date[day])
        irradiance = np.empty_like (data_location['AOI'])
        for i in range(len(data_location['AOI'])):    
            spot=gr.spot_grid(data_location['AOI'][i])
            gr.plot_grid(str(data_location['AOI'][i]),spot)
            if desp[i]!=0:
                cell_grid=cell.circular_cell(caracteristics_module['radius'], desp[i], 0)
            else:
                cell_grid=cell.circular_cell(caracteristics_module['radius'], desp[i], 3)
               
            area_illum,area_elect=cell.areas_intersection(spot,cell_grid)
            irradiance[i]=area_illum.sum()*data_location['POA_direct'][i]+data_location['POA_diffuse'][i]  
            gr.plot_grid(date[day],area_illum)
            gr.plot_grid(date[day],spot)
       
        plt.plot(irradiance,label='Irradiancia para electricidad')
        plt.plot(data_location['POA_diffuse'],label='difusa')
        plt.plot(data_location['POA_direct'],label='directa')
        
        
        plt.legend(loc=(0.5, 0))
        plt.xlabel('Hora del día')
        plt.ylabel('Irradiance [W/m2]')
        plt.title("Muesta irradiancias a lo largo del día "+ str(date[day]))
        
        plt.show()





