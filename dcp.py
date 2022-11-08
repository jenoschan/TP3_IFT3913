"""
here we create the plots for the DCP data

see seaborn documentation at:
https://seaborn.pydata.org/index.html 

see also: DCP_MustacheGraph.png for the result

"""


#using seaborn to plot boxplot from a csv file
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
dcp = df[' DCP']


sb.boxplot(x=dcp, showfliers=False)
plt.show()