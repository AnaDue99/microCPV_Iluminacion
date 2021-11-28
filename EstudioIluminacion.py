# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 21:00:45 2021

@author: Ana Dueñas
"""
import function as f
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Leemos los datos del CSV para los 12 AOI distintos
deg0,deg5, deg10,deg15,deg20,deg25,deg30,deg35,deg40,deg45,deg50,deg55,deg60 = f.read_aoi_data()	


for i in range(0,61,1):
    aoi_distribution=f.area_spot(i)
    f.plot_data_grid(i,aoi_distribution)


    
    

        

            
    


    
