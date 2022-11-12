"""
Using data from jfreechart-stats.csv
Building the Scatter plot for NoCom and DCP
Pearson's correlation coefficient - using scipy : https://scipy.org/install/

=> result in Terminal:
slope: -1.830022    intercept: 75.809529
r-squared: 0.237903
PearsonRResult(statistic=-0.4877529974573942, pvalue=4.41524835880053e-39)

"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
dcp = df[' DCP']
nocom = df[' NOCom']

sb.scatterplot(x=nocom, y=dcp)
plt.show() #close the window to continue

sb.regplot(x=nocom, y=dcp, order=2)
plt.show() #close the window to continue

#find linear regression
slope, intercept, r_value, p_value, std_err = ss.linregress(nocom, dcp)
print("slope: %f    intercept: %f" % (slope, intercept))
print("r-squared: %f" % r_value**2)



print(ss.mstats.pearsonr(nocom, dcp))
