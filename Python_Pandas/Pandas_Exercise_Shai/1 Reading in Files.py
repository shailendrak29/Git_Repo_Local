# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# Youtube link : https://www.youtube.com/watch?v=Mdq1WWSdUtw&t=1347s

# %%
# file_path = D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data

# %%
import pandas as pd

# %%
# 1. Read CSV

# %%
pd.read_csv("D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv")

# %%
#r - reads the file path as raw text 
# without r also my jupyter worked. in video it showed unicode error

# %%
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv")
# header populated automatically
#index shown automatically
# shift+Tab : This gives options about the command

# %%
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv", header = 1)  # picks first data as header
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv", header = None)  # Makes header as 0 and 1, similar to row index.

# %%
# can assign a new name to the Columns using names 
# header can be None, 0, 1 , irrespective of the name . it will behave as it is
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv", header = 0, names =['Country','Region'] )  # Makes header as 0 and 1, similar to row index.


# %%
df = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv")

# %%
df

# %%

# %%
#2. Read txt

# %%
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.txt")

# %%
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.txt",sep ='\t')

# %%
#better way is to read_table , works with and without separator

pd.read_table(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.txt")

# %%

# %%
# 3. Read JSON 

# %%
pd.read_json(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\json_sample.json")

# %%

# %%
# 4.Read Excel files 

# %%
pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx")

# by default it reads the first sheet 


# %%
pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')

# by default it reads the first sheet 
# Proving the Sheet_name allows us to pick the required sheet

# %%
# to see all the values in the dataframe

pd.set_option('display.max.rows',235)
pd.set_option('display.max.columns',40) # columns created bottom seek bar for json file, but for excle it did not create bottom seek bar 

# %%
pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')


# %%
pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx")

# %%
# 5. checking insights about the dataframe

# %%
df = pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')

# %%
df.info()

# %%
df.shape

# %%
df.head(10)

# %%
df.tail(10)

# %%
df['Rank'].tail(10)  #no dot bertween rank and df

# %%
# using indexes of rows
# loc -- looks for the string information
# iloc -- looks for integer value
# useful while changing the index

# %%
df.loc[224]

# %%
df.iloc[224]

# %%
df.loc['Uzbekistan']  # this will work when the index is changed to Country

# %%
