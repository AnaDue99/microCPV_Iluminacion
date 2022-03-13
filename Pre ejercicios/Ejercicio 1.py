# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:21:37 2021

Ejercicio 1.0
"ESTUDIO IRRADIANCIA  SALIENTE DE UNA LENTE BICONVEXA DEPENDIENDO DEL AOI"
@author: Ana Dueñas
"""


from pvlib import irradiance
from pvlib import location
import pandas as pd
import matplotlib.pyplot as plt
import math as m
from scipy.integrate import quad    

caracteristics_module={    
    'tilt':30,
    'surface_azimuth':180,
    'focal_distance': 5,
    'tam_module':7,
    'radius_multijunction':3,
    'radius_spot':3.001
    }

caracteristics={
    'lat':40.405655,
    'lon':-3.647649,
    'tz':'Europe/Madrid',
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

R=[]

for i in AOI:
    R.append(get_r(i,caracteristics_module['focal_distance']))

     
plt.plot(AOI,R,label='R')

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

        
"Estudiamos mejor, teniendo en cuenta el concepto de SPOT"
light_spot=[]
electricity_spot=[]


"Definición interseccion 2 circulos"
def f(x):
    return m.sqrt(abs((caracteristics_module['radius_multijunction'])**2-x**2))

def intersection(f,d, rs, rm):
   
    B=rm
    C=abs(d)-rs
    A=(B+C)/2
    match_surface=quad(f,A,B)
  
    if match_surface[0]<0:
        match_surface_ = 0 
          
    else:
        match_surface_=4*match_surface[0]
    return match_surface_

match_surface=[]
electric_efficiency=[]
for i in range(len(R)):
   match_surface.append(intersection(f,R[i],caracteristics_module['radius_spot'],caracteristics_module['radius_multijunction']))
   
   if match_surface==0:
        light_spot.append(total_irrad['poa_direct'][i])
        electricity_spot.append(0)
      
    
   else:
        electric_efficiency.append(match_surface[i]/(m.pi*(caracteristics_module['radius_spot'])**2))
        light_spot.append(total_irrad['poa_direct'][i]*(1-electric_efficiency[i]))
        electricity_spot.append(total_irrad['poa_direct'][i]*electric_efficiency[i])

        
for i in range(len(light)):
    light_spot[i]=light_spot[i]+total_irrad['poa_diffuse'][i]


Results_spot=pd.DataFrame({'Iluminación': light_spot,
                         'Electricidad': electricity_spot,
                         'Total':total_irrad['poa_global']})

plt.plot(AOI, electric_efficiency,label='eficiencia generación electrica')
plt.xlabel('AOI [º]')
plt.ylabel(' EFICIENCIA ELÉCTRICA [%1]')
plt.title('Eficiencia en tanto por 1')

plt.show()

plt.plot(AOI,light_spot, label='Light Irradiance')
plt.plot(AOI,electricity_spot, label='Electricity Irradiance')
plt.plot(AOI,total_irrad['poa_global'],label='total irradiance')
"plt.plot(AOI,total_irrad['poa_diffuse'],label='diffuse')"
plt.legend(loc=(1.0, 0))
plt.xlabel('AOI [º]')
plt.ylabel('Irradiance [W/m2]')
plt.title('Muesta irradiancias dependiendod el AOI de una lente TENIENDO EN CUENTA EL SPOT')
plt.show()




Results_spot.index = Results_spot.index.strftime("%H:%M")

Results_spot['Iluminación'].plot(label='Irradiancia para iluminación')
Results_spot['Electricidad'].plot( label='Irradiancia para electricidad')
Results_spot['Total'].plot( label='Irradiancia disponible total')

plt.legend(loc=(0.5, 0))
plt.xlabel('Hora del día')
plt.ylabel('Irradiance [W/m2]')
plt.title("Muesta irradiancias a lo largo del día de una lente TENIENDO EN CUENTA EL SPOT")

plt.show()





