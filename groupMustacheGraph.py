"""
groupMustacheGraph.py - boxplot of the data

Here we use seaborn to create a boxplot of all of the data
from jfreechart-stats.csv.

see seaborn documentation at:
https://seaborn.pydata.org/index.html 

see also: MustacheGraph.png for the result

"""


#using seaborn to plot boxplot from a csv file
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
nocom = df[' NOCom']
ncloc = df[' NCLOC']
dcp = df[' DCP']

#make 3 subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(9, 4))

#row 1 - boxplot of NOCom
sb.boxplot(x=nocom, ax=axes[0], showfliers=False)

#row 2 - boxplot of NCLOC
sb.boxplot(x=ncloc, ax=axes[1], showfliers=False)

#row 3 - boxplot of DCP
sb.boxplot(x=dcp, ax=axes[2], showfliers=False)

#individual plots
sb.boxplot(x=nocom, showfliers=False)

plt.show()