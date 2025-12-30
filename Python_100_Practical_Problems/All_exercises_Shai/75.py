# Plot data from the URL data

import pandas as pd
# import matplotlib.pyplot as plt
import pylab as plt

data_1 = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
print (data_1)

data_1.plot(x='x',y='y', kind = 'scatter')
data_1.plot(x='y',y='x', kind = 'scatter')
plt.show()