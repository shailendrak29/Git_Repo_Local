# Concatenate the values from both sites and display
# # https://pythonhow.com/media/data/sampledata_x_2.txt
# # https://pythonhow.com/media/data/sampledata.txt

#pandas solution

import pandas as pd
data_1 = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data_2 = pd.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")
print (data_1)
print (data_2)
data_3 = pd.concat([data_1,data_2]).drop_duplicates()
print (data_3)
data_3.to_csv("sample_data_3.csv", index=None)  # with index = None, only the data is populated and the index is dropped
