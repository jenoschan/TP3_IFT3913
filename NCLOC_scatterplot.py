"""
Using data from jfreechart-stats.csv
Building the Scatter plot for NoCom and NCLOC
Pearson's correlation coefficient - using scipy : https://scipy.org/install/

=> result in Terminal:
slope: 36.046998    intercept: -97.992499
r-squared: 0.510613
PearsonRResult(statistic=0.7145716586953953, pvalue=7.726928022388957e-100)


"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
ncloc = df[' NCLOC']
nocom = df[' NOCom']

sb.scatterplot(x=nocom, y=ncloc)
plt.show() #close the window to continue


sb.regplot(x=nocom, y=ncloc, order=2)
plt.show() #close the window to continue

#find linear regression
slope, intercept, r_value, p_value, std_err = ss.linregress(nocom, ncloc)
print("slope: %f    intercept: %f" % (slope, intercept))
print("r-squared: %f" % r_value**2)

print(ss.mstats.pearsonr(nocom, ncloc))
