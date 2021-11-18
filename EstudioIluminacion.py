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


aoi_distribution=f.area_spot(11)


f.plot_data_grid(deg0)
f.plot_data_grid(deg15)

f.plot_data_grid(aoi_distribution)
area_celula=f.definir_area_celula_rectanular(1,2,0,0,0.04)       
f.plot_data_grid(area_celula)
area_ilum,area_electricidad=f.calculo_diferencia_areas(deg0,area_celula)
f.plot_data_grid(area_ilum)
f.plot_data_grid(area_electricidad)

area_celula_=f.definir_area_celula_circular(1,0,-2,0.04)       
f.plot_data_grid(area_celula_)
area_ilum,area_electricidad=f.calculo_diferencia_areas(deg30,area_celula_)
f.plot_data_grid(area_ilum)
f.plot_data_grid(area_electricidad)



    
    

        

            
    


    
