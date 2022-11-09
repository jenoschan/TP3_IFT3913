"""
here we create the plots for the DCP data

see seaborn documentation at:
https://seaborn.pydata.org/index.html 

see also: DCP_MustacheGraph.png and DCP_MustacheGraph.csv
for the result

"""


#using seaborn to plot boxplot from a csv file
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv 

#read csv file
df = pd.read_csv('jfreechart-stats.csv')
dcp = df[' DCP']

q1 = np.percentile(dcp, 25)
q2 = np.percentile(dcp, 50)
q3 = np.percentile(dcp, 75)
iqr = q3 - q1

lowerWhisker = np.max([dcp.min(), q1 - 1.5 * iqr])
upperWhisker = np.min([dcp.max(), q3 + 1.5 * iqr])

with open('csv_results\\DCP_MustacheGraph.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['lowerWhisker', 'q1', 'q2', 'q3', 'upperWhisker'])
    writer.writerow([lowerWhisker, q1, q2, q3, upperWhisker])


sb.boxplot(x=dcp, showfliers=False)
plt.show()