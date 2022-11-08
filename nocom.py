"""
here we create the plots for the NOCom data

see seaborn documentation at:
https://seaborn.pydata.org/index.html 

see also: NoCOM_MustacheGraph.png for the result

"""


#using seaborn to plot boxplot from a csv file
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
nocom = df[' NOCom']


sb.boxplot(x=nocom, showfliers=False)
plt.show()