"""
Using data from jfreechart-stats.csv
Building the Scatter plot for NoCom and DCP
Pearson's correlation coefficient - using scipy : https://scipy.org/install/
=> result in Terminal:
PearsonRResult(statistic=-0.4877529974573942, pvalue=4.41524835880053e-39)
"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats.mstats as mstats

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
dcp = df[' DCP']
nocom = df[' NOCom']

sb.scatterplot(x=nocom, y=dcp)
plt.show()

print(mstats.pearsonr(nocom, dcp))
