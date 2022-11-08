"""
here we create the plots for the NCLOC data

see seaborn documentation at:
https://seaborn.pydata.org/index.html 

see also: NCLOC_MustacheGraph.png for the result

"""


#using seaborn to plot boxplot from a csv file
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
ncloc = df[' NCLOC']


sb.boxplot(x=ncloc, showfliers=False)
plt.show()