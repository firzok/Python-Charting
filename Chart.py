#--------------------------------------------------------------------------------------
#
#     $Source: TestFlakiness/Chart.py $
#
#  $Copyright: (c) 2018 Bentley Systems, Incorporated. All rights reserved. $
#
#--------------------------------------------------------------------------------------
import argparse
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt





#-------------------------------------------------------------------------------------------
# bsimethod                                     Firzok.Nadeem                    20/07/2018
#-------------------------------------------------------------------------------------------
#---Entry point of the Script ---#
if __name__ == '__main__':
    
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
    plt.savefig("test", dpi = 300)