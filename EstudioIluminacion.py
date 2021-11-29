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
    'tilt':30,
    'surface_azimuth':180,
    'radius':1.00
    }

caracteristics={
    'lat':40.405655,
    'lon':-3.647649,
    'tz':'Etc/GMT+2',
    'date':'21-06-2020',
    'temp':60
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

for i in AOI:
    if i<65 and i>-65:
        aoi=gr.spot_grid(i)
        area_illum,area_elect= cell.areas_intersection(aoi,cell_grid)
        gr.plot_grid(i,aoi)


    
    

        

            
    


    
