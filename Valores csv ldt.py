# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:21:45 2022

@author: anadu
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as interp
import module_AoiGrids as gr
import seaborn as sns
import numpy as np



path = f"28-Mar-2022\InsoPMMA_10deg\Intensity_10deg_0p7.csv"
Deg = pd.read_csv(path,index_col=0)

Final=Deg*1000/0.006405
deg=Deg.to_numpy()*1000/0.006405

Final.to_excel("Distribuciones angulares.xlsx")

print(deg.sum())

with sns.axes_style("white"):
    sns.heatmap(deg,vmin=0,  vmax=6, square=True,  cmap="YlGnBu_r")
    plt.title('a')
    plt.show()
    
x=[-90,-87,-85,-82,-80,-77,-75,-72,-70,-67,-65,-62,-60,-57,-55,-52,-50,-47,-45,-42,-40,-37,-35,-32,-30,-27,-25,-22,-20,-17,-15,-12,-10,-7,-5,-2,0,2,5,7,10,12,15,17,20,22,25,27,30,32,35,37,40,42,45,47,50,52,55,57,60,62,65,67,70,72,75,77,80,82,85,87,90]    
y=[-180,-177,-175,-172,-170,-167,-165,-162,-160,-157,-155,-152,-150,-147,-145,-142,-140,-137,-135,-132,-130,-127,-125,-122,-120,-117,-115,-112,-110,-97,-95,-92,-90,-87,-85,-82,-80,-77,-75,-72,-70,-67,-65,-62,-60,-57,-55,-52,-50,-47,-45,-42,-40,-37,-35,-32,-30,-27,-25,-22,-20,-17,-15,-12,-10,-7,-5,-2,0,2,5,7,10,12,15,17,20,22,25,27,30,32,35,37,40,42,45,47,50,52,55,57,60,62,65,67,70,72,75,77,82,85,87,90,92,95,97,100,112,115,117,120,122,125,127,130,132,135,137,140,142,145,147,150,152,155,57,160,162,165,167,170,172,175,177,180]   



ldt=interp(Final.index,Final["-123.58"],k=3)


a=ldt(x)
a=pd.DataFrame(a)
a.index=x







