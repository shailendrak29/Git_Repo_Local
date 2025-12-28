# Alternate way to read csv file using request

import io
import pandas
import requests

r = requests.get("https://pythonhow.com/media/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2]).drop_duplicates()
print (data12)
# data12.to_csv("sampledata12.txt", index=None)