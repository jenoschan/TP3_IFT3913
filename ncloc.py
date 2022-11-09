"""
here we create the plots for the NCLOC data

see seaborn documentation at:
https://seaborn.pydata.org/index.html 

see also: NCLOC_MustacheGraph.png and NCLOC_MustacheGraph.csv 
for the results

"""


#using seaborn to plot boxplot from a csv file
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
ncloc = df[' NCLOC']

q1 = np.percentile(ncloc, 25)
q2 = np.percentile(ncloc, 50)
q3 = np.percentile(ncloc, 75)
iqr = q3 - q1

lowerWhisker = np.max([ncloc.min(), q1 - 1.5 * iqr])
upperWhisker = np.min([ncloc.max(), q3 + 1.5 * iqr])

with open('csv_results\\NCLOC_MustacheGraph.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['lowerWhisker', 'q1', 'q2', 'q3', 'upperWhisker'])
    writer.writerow([lowerWhisker, q1, q2, q3, upperWhisker])

plot = sb.boxplot(x=ncloc, showfliers=False)
plt.show()