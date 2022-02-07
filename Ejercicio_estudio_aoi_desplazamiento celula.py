# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:21:08 2022

@author: anadu
"""

"""
Se va a analizar y  llegar a conclusiones de qué irradiancia se consigue 
dependiendo del angulo de incidencia y de la posición de la célula

Angulos de incidencia: 0,10,15,20,25,30,35,40,45,50,55,60
Posición celula: paso de 0.02 mm
"""


import module_Cell as cell
import module_AoiGrids as gr
import matplotlib.pyplot as plt
import numpy as np

caracteristics_module={    
    'tilt':0,
    'surface_azimuth':180,
    'radius':1.2
    }

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

desp=np.arange(0, 3, 0.01)

for i in desp:
    irradiance_aoi_0.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 0))
    irradiance_aoi_5.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 5))
    irradiance_aoi_10.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 10))
    irradiance_aoi_15.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 15))
    irradiance_aoi_20.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 20))
    irradiance_aoi_25.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 25))
    irradiance_aoi_30.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 30))
    irradiance_aoi_35.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 35))
    irradiance_aoi_40.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 40))
    irradiance_aoi_45.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 45))
    irradiance_aoi_50.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 50))
    irradiance_aoi_55.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 55))
    irradiance_aoi_60.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 60))
    
    
    
    
    
plt.plot(desp,irradiance_aoi_0,label='aoi 0')
plt.plot(desp,irradiance_aoi_5,label='aoi 5')
plt.plot(desp,irradiance_aoi_10,label='aoi 10')
plt.plot(desp,irradiance_aoi_15,label='aoi 15')
plt.plot(desp,irradiance_aoi_20,label='aoi 20')
plt.plot(desp,irradiance_aoi_25,label='aoi 25')
plt.plot(desp,irradiance_aoi_30,label='aoi 30')
plt.plot(desp,irradiance_aoi_35,label='aoi 35')
plt.plot(desp,irradiance_aoi_40,label='aoi 40')
plt.plot(desp,irradiance_aoi_50,label='aoi 50')
plt.plot(desp,irradiance_aoi_55,label='aoi 55')
plt.plot(desp,irradiance_aoi_60,label='aoi 60')


plt.legend(loc=(1, 0))
plt.xlim(-0.1,3.1)
plt.xlabel('Desplazamiento[mm]')
plt.ylabel('Irradiance [W/m2]')
plt.title("Muesta irradiancias iluminacion(fuera celula) para distintos AOI y variación desplazamiento")

plt.show()











