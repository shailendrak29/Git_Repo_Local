# Get data from wb page https://pythonhow.com/media/data/sampledata.txt

import pandas

data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data_2 = data*2
data_2.to_csv("sampledata_x_2.txt", index=None)