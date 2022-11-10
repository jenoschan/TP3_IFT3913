"""
Using data from jfreechart-stats.csv
Building the Scatter plot for NoCom and NCLOC
Pearson's correlation coefficient - using scipy : https://scipy.org/install/
=> result in Terminal:
PearsonRResult(statistic=0.7145716586953953, pvalue=7.726928022388957e-100)
"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats.mstats as mstats

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
ncloc = df[' NCLOC']
nocom = df[' NOCom']

sb.scatterplot(x=nocom, y=ncloc)
plt.show()

print(mstats.pearsonr(nocom, ncloc))
