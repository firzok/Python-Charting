# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:34:00 2018

@author: Firzok.Nadeem
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



df=pd.read_csv("NewlyAddedTestsReport.csv")

X = np.array(df.Component.unique())

Y = np.unique(df.Component, return_counts=True)[1]
size = len(df.Component.unique())
plt.figure(figsize=(size+3,size+3))
sns.set_style("whitegrid")


groupedvalues=df.groupby('Component').sum().reset_index()

g = sns.barplot(x=X, y=Y, palette=sns.color_palette("cubehelix", len(df.Component.unique()) + 5))


for index, row in groupedvalues.iterrows():
    g.text(row.name, Y[index] + 0.5, Y[index], color='black', ha="center", weight="bold")


sns.despine(left=True)
plt.savefig("test")