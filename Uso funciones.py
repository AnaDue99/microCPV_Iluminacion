# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:31:32 2022

@author: anadu
"""

import module_Cell as cell
import module_AoiGrids as gr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as interp


caracteristics_module={    
    'tilt':0,
    'surface_azimuth':180,
    'radius':0.6,
    'area':179*10**-6
    }
caracteristics={
    'lat':40.544,
    'lon':-3.613,
    'tz':'Etc/GMT+2',
    'date':'2021-06-21',
    }

desp=np.arange(0, 3, 0.01)
f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60=cell.function(desp,caracteristics_module['radius'])

data_location=gr.get_data_location(caracteristics,caracteristics_module,caracteristics['date']) 

illum_module=[]
for i in range(len(data_location['AOI'])):
    irrad_distribution=cell.irrad(0,data_location['AOI'][i],f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60)*data_location['POA_direct'][i]
    illum_module.append(cell.from_irrad_to_ilum(float(irrad_distribution),caracteristics_module['area']))
    
illum_module=illum_module+cell.from_irrad_to_ilum(data_location['POA_diffuse'],caracteristics_module['area'])

plt.plot(illum_module)
plt.plot(cell.from_irrad_to_ilum(data_location['POA_diffuse'],caracteristics_module['area']))
plt.xlabel('horas del día')
plt.ylabel('Lux de potencia de iluminacion')
plt.title("Muesta lux para el 21 de junio 2020 una sola célula")

plt.show()


illum_goal=1600
illum_module=[]
desp_cell=[]
for i in range(len(data_location['AOI'])):
    illum_module.append(cell.adjust(illum_goal,data_location['AOI'][i],caracteristics_module['area'],data_location['POA_direct'][i],data_location['POA_diffuse'][i],
                                    f_0,f_5,f_10,f_15,f_20,f_25,f_30,f_35,f_40,f_45,f_50,f_55,f_60))
   


plt.plot(illum_module)
plt.plot(cell.from_irrad_to_ilum(data_location['POA_diffuse'],caracteristics_module['area']))
plt.xlabel('horas del día')
plt.ylabel('Lumen de iluminancia')
plt.title("Muesta lumen para el 21 de junio 2020 una sola célula")

plt.show()