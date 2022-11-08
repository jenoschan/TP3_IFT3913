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
sb.boxplot(x=nocom, ax=axes[0])

#row 2 - boxplot of NCLOC
sb.boxplot(x=ncloc, ax=axes[1])

#row 3 - boxplot of DCP
sb.boxplot(x=dcp, ax=axes[2])

plt.show()