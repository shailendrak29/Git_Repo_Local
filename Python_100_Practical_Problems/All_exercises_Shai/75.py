# Plot data from the URL data

import pandas as pd
import matplotlib.pyplot as plt
data_1 = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt",columns=['X', 'Y'])
print (data_1)

data_1.plot(x,y)