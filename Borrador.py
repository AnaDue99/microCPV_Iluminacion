# -*- coding: utf-8 -*-
"""
Definición un dispositivo fotovoltaico (con una curva IV, con dimensiones,
                                        eficiencia, posición...) 
y ver cual sería la potencia generada. 
Para ello se calcula el recurso solar sobre el dispositivo, y después se aplica
 ese recurso para transformar la curva IV del dispositivo. 
 

@author: Ana Dueñas
"""

from pvlib import location
from pvlib import irradiance
from pvlib import pvsystem
import pandas as pd
import matplotlib.pyplot as plt

"Vamos a definir un lugar del planeta: ETSIDI"
tz='Etc/GMT+2'
lat, long= 40.405655, -3.700292

"Creamos objeto con la localización"
site = location.Location(lat, long, tz=tz)

def get_irradiance(site_location, date, tilt, surface_azimuth):
    # Creates one day's worth of 30 min intervals
    times = pd.date_range(date, freq='30min', periods=2*24,
                          tz=site_location.tz)
    # Generate clearsky data using the Ineichen model, which is the default
    # The get_clearsky method returns a dataframe with values for GHI, DNI,
    # and DHI
    clearsky = site_location.get_clearsky(times)
    # Get solar azimuth and zenith to pass to the transposition function
    solar_position = site_location.get_solarposition(times=times)
   
    
    # Use the get_total_irradiance function to transpose the GHI to POA
    POA_irradiance = irradiance.get_total_irradiance(
        surface_tilt=tilt,
        surface_azimuth=surface_azimuth,
        
        dni=clearsky['dni'],
        ghi=clearsky['ghi'],
        dhi=clearsky['dhi'],
        solar_zenith=solar_position['apparent_zenith'],
        solar_azimuth=solar_position['azimuth'],
        )
    
    aoi=irradiance.aoi(POA_irradiance[''],surface_azimuth,solar_position['apparent_zenith'],solar_position['azimuth'])
    # Return DataFrame with only GHI, DHI, POA & AOI
    return pd.DataFrame({'GHI': clearsky['ghi'],
                         'DHI': clearsky['dhi'],
                         'AOI': POA_irradiance['aoi'],
                         'POA': POA_irradiance['poa_global']})


"Calculamos la irradiance para el solsticio de verano y de invierno"
"tilt es el angulo de inclinación"
tilt=25 

"El azimuth de la superficie es la orientación del módulo respecto el N,S,E,O"
"Igual que el azimuth solar es la orientación del sol respecto al N,S,E,0"
    
surface_azimuth=180 
summer_irradiance = get_irradiance(site, '06-20-2021', tilt, surface_azimuth)
winter_irradiance = get_irradiance(site, '12-21-2020', tilt, surface_azimuth)

"Dibujo"

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
summer_irradiance['GHI'].plot(ax=ax1, label='GHI')
summer_irradiance['POA'].plot(ax=ax1, label='POA')
winter_irradiance['GHI'].plot(ax=ax2, label='GHI')
winter_irradiance['POA'].plot(ax=ax2, label='POA')
ax1.set_xlabel('Time of day (Summer)')
ax2.set_xlabel('Time of day (Winter)')
ax1.set_ylabel('Irradiance ($W/m^2$)')
ax1.legend()
ax2.legend()
plt.show()



"Cálculo de la efectiva"

airmass_absolute=site.get_airmass( None,model='kastenyoung1989')
effective_radiance=pvsystem.sapm_effective_irradiance(summer_irradiance['POA'], summer_irradiance['DHI'], airmass_absolute,summer_irradiance['AOI'] )




