# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:22:12 2024

@author: Jack

Source: https://glasspy.readthedocs.io/en/latest/#
"""

#importing required packages
import pandas as pd
from glasspy.data import SciGlass

#import all database into a df
source = SciGlass()
df = source.data

filters=df.columns.levels[0]
#should return 'elements', 'compounds', 'property', 'metadata'
#these can be used to subset the data

#the data can be subset for filtering
subset1 = df["elements"]
subset2 = df["compounds"]
subset3 = df["property"]
subset4 = df["metadata"]


#list all propertoes for filtering
properties = SciGlass.available_properties()

#extracting all columns containing viscosity
df_1 = subset3.filter(like="Viscosity", axis=1)

#extracting "Tg" column
df_2 = subset3.loc[:, ["Tg"]]

#merging into one
df = pd.merge(df_1, df_2, on='ID')

#subsetting by where Viscosity773K is not NaN
df = df[df["Viscosity773K"].notna()]

#subsetting by Tg>600
df = df[df["Tg"]>600]