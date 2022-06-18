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



path = f"28-Mar-2022\InsoPMMA_0deg\Intensity_0deg.csv"
Deg = pd.read_csv(path,index_col=0)

Final=Deg*1000/0.006405
deg=Deg.to_numpy()*1000/0.006405

Final.to_excel("Distribuciones angulares.xlsx","50")

print(deg.sum())

with sns.axes_style("white"):
    sns.heatmap(deg,vmin=0,  vmax=6, square=True,  cmap="YlGnBu_r")
    plt.title('a')
    plt.show()
    







