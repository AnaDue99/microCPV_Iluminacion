# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:54:50 2022

@author: anadu
"""
import numpy as np
from pvlib import location
from pvlib import irradiance
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as interp


path = f"OptiMesh_0deg.csv"
Deg = pd.read_csv(path)

ANGULO=[-0.1665,1.7910,3.5821,5.3731,7.1642,8.9552,10.7463,12.5373,14.3284,16.1194,17.9104,19.7015,21.4925,23.2836,25.0746,26.8657,28.6567,30.4478,32.2388,34.0299,35.8209,37.6119,39.4030,41.1940,42.9851,44.7761,46.5672]
CD=[0.3096,0.2800,0.2586,0.2646,0.2604,0.2541,0.2492,0.2311,0.2114,0.2186,0.2032,0.1640,0.1561,0.1882,0.1764,0.1258,0.0918,0.0947,0.1148,0.1048,0.0502,0.0098,0.0083,0.0049,0.0003,0.0000,0.0000]


ldt=interp(ANGULO,CD,k=3)


data=range(0,180,5)
a=ldt(data)

import module_Cell as cell
import module_AoiGrids as gr

spot=gr.spot_grid(0)
