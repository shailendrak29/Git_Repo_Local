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
df = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population.csv")
#if a xls file is read, it will give unicode error


# %%
df

# %%
#1 Filter based on numeric column value

# %%
df[df["Rank"] <=10]

# %%
# 2. Filter based on list values. Similiar to IN function of SQL
# using isin()

# %%
specific_countries = ['Bangladesh','Brazil']
df[df["Country"].isin(specific_countries)]

# %%
# 3 Filter 
# Contains is more like "LIKE". %word%

# %%
df[df["Country"].str.contains('United')]

# %%

# %%
#4. CHange the Index to specific Column and then filter based on it

# %%
df2 = df.set_index('Country')

# %%
df2

# %%

# %%
# 5.Filter based on the Index 

# %%
#5.1 filter + Items

# %%
df2.filter(items = ['Continent','CCA3'])  # this is like select statement with index column attached

# %%
# 5.1.1 play of axis.
# Axis determines where the items will be searched.
# By default axis = 1, i.e. it searched for columns
# axis = 0, searches the index rows

# %%
df2.filter(items = ['Continent','CCA3'], axis = 1)

# %%
df2.filter(items = ['Continent','CCA3'], axis = 0)

# %%
df2.filter(items = ['Zimbabwe','Algeria'], axis = 0)

# %%
#5.2 filter + Like 
# filter like on Index column ( if its not index column we would have to go  square bracket route.
# so reading filter could become difficult, since the Index is not explicitly mentioned


# %%
df2.filter(like = 'United', axis = 0)

# %%
# Note : how to see what is the current index of the dataframe? 

# %%
df2.index

# %%
df2.index.name

# %%

# %%
# 5.3 Filter using loc
# Gets data in transposed manner for specific value of Index Column
# Can it get multiple values ?

# %%
df2.loc['United States']

# %%
# df2.loc['United'] 

# this gives error as United is not a value in Country columns

# %%
# 5.4 Filter using iloc 
# the inherent index value is the number, iloc still looks for that value to pick details 

# %%
df2.iloc[3]

# %%

# %%

# %%
# Order by

# %%
df

# %%
df2

# %%
#1. Order on a single column
# using sort_value by

# %%
df[df['Rank'] < 10].sort_values(by ='Rank', ascending=True)

# %%
df[df['Rank'] < 10].sort_values(by ='Rank', ascending=False)

# %%
# 2. Order by - sort multiple columns 
# here the ascending is applied to all the sorted columns

# %%
df[df['Rank'] < 10].sort_values(by =['Continent','Country'], ascending=True)

# %%
#2.1 Order by - sort multiple columns, with different ascending and descending preferences

# %%
df[df['Rank'] < 10].sort_values(by =['Continent','Country'], ascending=[True,False])

# %%
