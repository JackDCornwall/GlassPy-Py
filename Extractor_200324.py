# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:20:06 2024

@author: Jack
"""

#importing required packages
import pandas as pd
from glasspy.data import SciGlass


#import all database into a df
source = SciGlass()

raw = source.data

#the data can be subset for filtering
compounds = raw["compounds"]
properties = raw["property"]

#extracting "Tg" column
Tg_col = properties.loc[:, ["Tg"]]

#merging into one
df = pd.merge(compounds, Tg_col, on='ID')

# dropping rows where Tg is nan
df.dropna(subset=['Tg'], inplace=True)

#finding all columns only containing zeroes
zero_cols = df.columns[(df == 0).all()]
#zero_cols = df.columns[(df.to_numpy().sum(axis=0) == 0)]

#dropping all columns only containing zeroes
df.drop(zero_cols, axis=1, inplace=True)

#exporting dataframe
df.to_csv("export.csv", index=False)

raw.to_csv("out.csv")
