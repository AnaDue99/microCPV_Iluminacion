# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:21:37 2021
"ESTUDIO IRRADIANCIA  SALIENTE DE UNA LENTE BICONVEXA DEPENDIENDO DEL AOI"
@author: Ana Dueñas
"""


from pvlib import irradiance
from pvlib import location
import pandas as pd
import matplotlib.pyplot as plt
import math as m


caracteristics_module={    
    'tilt':30,
    'surface_azimuth':180,
    'focal_distance': 5,
    'tam_module':30
    }

caracteristics_ETSIDI_summer={
    'lat':40.405655,
    'lon':-3.700292,
    'tz':'Etc/GMT+2',
    'date':'21-06-2020',
    'temp':60
    }

"Creamos objeto con la localización"
site = location.Location(caracteristics_ETSIDI_summer['lat'], 
                         caracteristics_ETSIDI_summer['lon'],
                        caracteristics_ETSIDI_summer['tz'])
                                                      
times = pd.date_range(caracteristics_ETSIDI_summer['date'], freq='10min', periods=6*24,
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

min_AOI=min(AOI)
max_AOI=max(AOI)

def get_max_aoi(tam_module,focal_dist):
    MAX_AOI=m.atan(tam_module/focal_dist)*180/m.pi
    return MAX_AOI
MAX_AOI=get_max_aoi(caracteristics_module['tam_module'],caracteristics_module['focal_distance'])    
    
light=[]
electricity=[]

for x in range(len(AOI)):    
    if AOI[x]>MAX_AOI:
        light.append(total_irrad['poa_direct'][x])
        electricity.append(0)
        AOI[x]=MAX_AOI
    else:
        electricity.append(total_irrad['poa_direct'][x])
        light.append(0)

for x in range(len(AOI)):
    if AOI[x]==min_AOI:
        a=x
        for x in range(a,len(AOI)):
          AOI[x]=-AOI[x]

for i in range(len(light)):
    light[i]=light[i]+total_irrad['poa_diffuse'][i]

    
    
    
AOI.index = AOI.index.strftime("%H:%M")        
plt.plot(AOI)
plt.xlabel('Horario  verano')
plt.ylabel('AOI (DEG)')
plt.title('AOI a lo largo del dia')
plt.show()



DifAzimuths=caracteristics_module['surface_azimuth']-solar_position['azimuth']
DifAzimuths=DifAzimuths.tolist()
[float(i) for i in DifAzimuths]
"La distancia entre célula y lente será la distancia focal"

def get_r(AOI,focal_dist):
    r=focal_dist*m.tan(AOI*m.pi/180)
    "por el convenio establecido:"
    r=-r
    return r

def get_x(_r,DifAzimuths):
    x=_r*m.cos(DifAzimuths*m.pi/180)
    return x
def get_y(_r,DifAzimuths):
    y=_r*m.sin(DifAzimuths*m.pi/180)
    return y

R=[]
X=[]
Y=[]

for i in AOI:
    R.append(get_r(i,caracteristics_module['focal_distance']))

[float(i) for i in R]

for i in range(len(R)):
    X.append(get_x(R[i],DifAzimuths[i]))
    Y.append(get_y(R[i],DifAzimuths[i]))

    

    
plt.plot(AOI,R,label='R')
"plt.plot(AOI,X,label='X')"
"plt.plot(AOI,Y,label='Y')"
plt.legend(loc=(1.0, 0))
plt.xlabel('AOI (º)')
plt.ylabel('R (mm)')
plt.title('Movimiento del foco dependiendo del AOI a lo largo del dia')
plt.show()
plt.gcf().set_tight_layout(True)

plt.plot(AOI,light, label='Light Irradiance')
plt.plot(AOI,electricity, label='Electricity Irradiance')
plt.plot(AOI,total_irrad['poa_global'],label='total irradiance')
"plt.plot(AOI,total_irrad['poa_diffuse'],label='diffuse')"
plt.legend(loc=(1.0, 0))
plt.xlabel('AOI [º]')
plt.ylabel('Irradiance [W/m2]')
plt.title('Muesta irradiancias dependiendod el AOI de una lente')
plt.show()
plt.gcf().set_tight_layout(True)

        


