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
desp=np.arange(0, 3, 0.02)

for i in desp:
    irradiance_aoi_0.append(cell.irradiance_cell(caracteristics_module['radius'], i, 0, 0))

plt.plot(desp,irradiance_aoi_0)
plt.legend(loc=(0.5, 0))
plt.xlabel('Desplazamiento[mm]')
plt.ylabel('Irradiance [W/m2]')
plt.title("Muesta irradiancias iluminacion(fuera celula) para un AOI de 0º y variación desplazamiento")

plt.show()