# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 21:00:45 2021

@author: Ana Dueñas
"""
import module_Cell as cell
import module_AoiGrids as gr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pvlib import location
from pvlib import irradiance

caracteristics_module={    
    'tilt':0,
    'surface_azimuth':180,
    'radius':1.2
    }

caracteristics={
    'lat':40.405655,
    'lon':-3.647649,
    'tz':'Etc/GMT-2',
    'date':'2021-02-2',
    
    }
"Creamos objeto con la localización"
site = location.Location(caracteristics['lat'], 
                         caracteristics['lon'],
                        caracteristics['tz'])
                                                      
times = pd.date_range(caracteristics['date'], freq='10min', periods=6*24,
                      tz=site.tz)
clearsky = site.get_clearsky(times)
solar_position = site.get_solarposition(times)
    
"Calculamos la irradiancia que le llega"
"         CARACTERISTICAS DEL      MODULO FISICAS"

  
total_irrad=irradiance.get_total_irradiance( 
    surface_tilt=caracteristics_module['tilt'],
    surface_azimuth=caracteristics_module['surface_azimuth'],
    dni=clearsky['dni'],
    ghi=clearsky['ghi'],
    dhi=clearsky['dhi'],
    solar_zenith=solar_position['apparent_zenith'],
    solar_azimuth=solar_position['azimuth'])
    
    
"GET AOI"
AOI=irradiance.aoi( caracteristics_module['tilt'],
                   caracteristics_module['surface_azimuth'],
                   solar_position['apparent_zenith'], 
                   solar_position['azimuth'])


cell_grid=cell.circular_cell(caracteristics_module['radius'], 0, 0)
gr.plot_grid('CELULA CIRCULAR',cell_grid)

AOI=gr.transform_aoi(AOI)
AOI.index = AOI.index.strftime("%H:%M")
irradiance= np.empty_like (AOI)


for i in range(len(times)):
    irradiance[i]=cell.irradiance_cell(caracteristics_module['radius'], 0, 0, AOI[i])




plt.plot(times,irradiance,label='Irradiancia para electricidad')
plt.plot(times,total_irrad['poa_diffuse'],label='difusa')
plt.plot(times,total_irrad['poa_direct'],label='directa')


plt.legend(loc=(0.5, 0))
plt.xlabel('Hora del día')
plt.ylabel('Irradiance [W/m2]')
plt.title("Muesta irradiancias a lo largo del día")

plt.show()
      


            
    


    
