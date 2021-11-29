# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:50:25 2021

@author: anadu
"""

import module_Cell as cell
import module_AoiGrids as gr
import pandas as pd

#Leemos del CSV los datos
Deg0 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_0deg\OptiMesh_0deg.csv")   
Deg5 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_5deg\OptiMesh_5deg.csv") 
Deg10 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_10deg\OptiMesh_10deg.csv")   
Deg15 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_15deg\OptiMesh_15deg.csv") 
Deg20 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_20deg\OptiMesh_20deg.csv")   
Deg25 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_25deg\OptiMesh_25deg.csv") 
Deg30 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_30deg\OptiMesh_30deg.csv")   
Deg35 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_35deg\OptiMesh_35deg.csv") 
Deg40 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_40deg\OptiMesh_40deg.csv")   
Deg45 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_45deg\OptiMesh_45deg.csv") 
Deg50 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_50deg\OptiMesh_50deg.csv")   
Deg55 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_55deg\OptiMesh_55deg.csv") 
Deg60 = pd.read_csv("spots inso 29-Oct-2021\InsoPMMA_60deg\OptiMesh_60deg.csv")

#Pasamos la columna NaN a indice. 

Deg5.set_index('NaN',inplace=True)
Deg10.set_index('NaN',inplace=True)
Deg15.set_index('NaN',inplace=True)
Deg20.set_index('NaN',inplace=True)
Deg25.set_index('NaN',inplace=True)
Deg30.set_index('NaN',inplace=True)
Deg35.set_index('NaN',inplace=True)
Deg40.set_index('NaN',inplace=True)
Deg45.set_index('NaN',inplace=True)
Deg50.set_index('NaN',inplace=True)
Deg55.set_index('NaN',inplace=True)
Deg60.set_index('NaN',inplace=True)

#Se ha preferido trabajar con matrices aunque no descarto intentarlo con dataframe luego
deg0=Deg0.to_numpy()
deg5=Deg5.to_numpy()
deg10=Deg10.to_numpy()
deg15=Deg15.to_numpy()
deg20=Deg20.to_numpy()
deg25=Deg25.to_numpy()
deg30=Deg30.to_numpy()
deg35=Deg35.to_numpy()
deg40=Deg40.to_numpy()
deg45=Deg45.to_numpy()
deg50=Deg50.to_numpy()
deg55=Deg55.to_numpy()
deg60=Deg60.to_numpy()