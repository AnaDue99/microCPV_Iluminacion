# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:05:15 2021

@author: Ana Dueñas


"""

import pandas as pd

import matplotlib.pyplot as plt

naive_times = pd.date_range(start='2015', end='2016', freq='1h')



coordinates = [(30, -110, 'Tucson', 700, 'Etc/GMT+7'),
               (35, -105, 'Albuquerque', 1500, 'Etc/GMT+7'),
               (40, -120, 'San Francisco', 10, 'Etc/GMT+8'),
               (50, 10, 'Berlin', 34, 'Etc/GMT-1')]


import pvlib


sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')

sapm_inverters = pvlib.pvsystem.retrieve_sam('cecinverter')

module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']

inverter = sapm_inverters['ABB__MICRO_0_25_I_OUTD_US_208__208V_']

temperature_model_parameters = pvlib.temperature.TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']


temp_air = 20

wind_speed = 0
