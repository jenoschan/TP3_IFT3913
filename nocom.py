"""
here we create the plots for the NOCom data

see seaborn documentation at:
https://seaborn.pydata.org/index.html 

see also: NoCOM_MustacheGraph.png and NoCOM_MustacheGraph.csv
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
nocom = df[' NOCom']

q1 = np.percentile(nocom, 25)
q2 = np.percentile(nocom, 50)
q3 = np.percentile(nocom, 75)
iqr = q3 - q1

lowerWhisker = np.max([nocom.min(), q1 - 1.5 * iqr])
upperWhisker = np.min([nocom.max(), q3 + 1.5 * iqr])

with open('csv_results\\NOCom_MustacheGraph.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['lowerWhisker', 'q1', 'q2', 'q3', 'upperWhisker'])
    writer.writerow([lowerWhisker, q1, q2, q3, upperWhisker])


sb.boxplot(x=nocom, showfliers=False)
plt.show()