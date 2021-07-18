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

"RECURSO SOLAR SOBRE EL DISPOSITIVO"
def get_recurso(lat,lon,tz,date,tilt,surface_azimuth):

    "Creamos objeto con la localización"
    site = location.Location(lat, lon, tz=tz)
    times = pd.date_range(date, freq='10min', periods=6*24,
                          tz=site.tz)
    clearsky = site.get_clearsky(times)
    solar_position = site.get_solarposition(times)


    "Calculamos la irradiancia que le llega"
    "         CARACTERISTICAS DEL      MODULO FISICAS"

  
    total_irrad=irradiance.get_total_irradiance( 
        surface_tilt=tilt,
        surface_azimuth=surface_azimuth,
        dni=clearsky['dni'],
        ghi=clearsky['ghi'],
        dhi=clearsky['dhi'],
        solar_zenith=solar_position['apparent_zenith'],
        solar_azimuth=solar_position['azimuth'])
    
    print(total_irrad['poa_direct'])
    return pd.DataFrame({'POA': total_irrad['poa_global'],
                         'POA_diffuse': total_irrad['poa_diffuse'],
                         'POA_direct':total_irrad['poa_direct']})
"CURVA IV Y POTENCIA"
def get_pot(poa_direct,temp,alpha_sc,a_ref,I_L_ref,I_o_ref,R_sh_ref,R_s):
           
    IL, I0, Rs, Rsh, nNsVth = pvsystem.calcparams_desoto(
        effective_irradiance=poa_direct,
        temp_cell=temp,
        alpha_sc=alpha_sc,
        a_ref=a_ref,
        I_L_ref=I_L_ref,
        I_o_ref=I_o_ref,
        R_sh_ref=R_sh_ref,
        R_s=R_s,
        EgRef=1.121,
        dEgdT=-0.0002677
    )
    curve_info = pvsystem.singlediode(
        photocurrent=IL,
        saturation_current=I0,
        resistance_series=Rs,
        resistance_shunt=Rsh,
        nNsVth=nNsVth,
        ivcurve_pnts=50,
        method='lambertw'
    )
    
    print(pd.DataFrame({
    'i_sc': curve_info['i_sc'],
    'v_oc': curve_info['v_oc'],
    'i_mp': curve_info['i_mp'],
    'v_mp': curve_info['v_mp'],
    'p_mp': curve_info['p_mp'],
    }))
    

    return curve_info


caracteristics_ETSIDI_summer={
    'lat':40.405655,
    'lon':-3.700292,
    'tz':'Etc/GMT+2',
    'date':'21-06-2020',
    'temp':35
    }

caracteristics_ETSIDI_winter={
    'lat':40,
    'lon':-3.700292,
    'tz':'Etc/GMT+2',
    'date':'21-12-2020',
    'temp':10
    }

caracteristics_module={
    'tilt':30,
    'surface_azimuth':180,   
    'alpha_sc':0.0046,
    'a_ref':42.4,
    'I_L_ref': 5.114,
    'I_o_ref': 8.196e-10,
    'R_sh_ref': 381.68,
    'R_s': 1.065
    }

summer_recurso_ETSIDI=get_recurso(caracteristics_ETSIDI_summer['lat'],
                                  caracteristics_ETSIDI_summer['lon'],
                                  caracteristics_ETSIDI_summer['tz'],
                                  caracteristics_ETSIDI_summer['date'],
                                  caracteristics_module['tilt'],
                                  caracteristics_module['surface_azimuth'])
                                 

summer_potencia_ETSIDI=get_pot(summer_recurso_ETSIDI['POA_direct'], 
                                caracteristics_ETSIDI_summer['temp'],
                                caracteristics_module['alpha_sc'],
                                caracteristics_module['a_ref'],
                                caracteristics_module['I_L_ref'],
                                caracteristics_module['I_o_ref'],
                                caracteristics_module['R_sh_ref'],
                                caracteristics_module['R_s'])
                                    

winter_recurso_ETSIDI=get_recurso(caracteristics_ETSIDI_summer['lat'],
                                  caracteristics_ETSIDI_summer['lon'],
                                  caracteristics_ETSIDI_summer['tz'],
                                  caracteristics_ETSIDI_summer['date'],
                                  caracteristics_module['tilt'],
                                  caracteristics_module['surface_azimuth'])
                                 

winter_potencia_ETSIDI=get_pot(winter_recurso_ETSIDI['POA_direct'], 
                                caracteristics_ETSIDI_summer['temp'],
                                caracteristics_module['alpha_sc'],
                                caracteristics_module['a_ref'],
                                caracteristics_module['I_L_ref'],
                                caracteristics_module['I_o_ref'],
                                caracteristics_module['R_sh_ref'],
                                caracteristics_module['R_s'])

"Dibujo recurso radiación"
# Convert Dataframe Indexes to Hour:Minute format to make plotting easier
summer_recurso_ETSIDI.index = summer_recurso_ETSIDI.index.strftime("%H:%M")
winter_recurso_ETSIDI.index = winter_recurso_ETSIDI.index.strftime("%H:%M")


fig, (ax1,ax2) = plt.subplots(1,2, sharey=True)

summer_recurso_ETSIDI['POA'].plot(ax=ax1, label='POA_GLOBAL')
summer_recurso_ETSIDI['POA_diffuse'].plot(ax=ax1, label='POA_DIFFUSE')
summer_recurso_ETSIDI['POA_direct'].plot(ax=ax1, label='POA_DIRECT')

winter_recurso_ETSIDI['POA'].plot(ax=ax2, label='POA_GLOBAL')
winter_recurso_ETSIDI['POA_diffuse'].plot(ax=ax2, label='POA_DIFFUSE')
winter_recurso_ETSIDI['POA_direct'].plot(ax=ax2, label='POA_DIRECT')


ax1.set_xlabel('Time of day (Summer)')
ax2.set_xlabel('Time of day (Winter)')
ax1.set_ylabel('Irradiance ($W/m^2$)')

ax1.legend()
ax2.legend()
plt.show()
        
"CURVES IV dibujo"   






