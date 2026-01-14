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

# %% [markdown]
# [Youtube link](https://www.youtube.com/watch?v=Mdq1WWSdUtw&list=WL&index=93&t=2495s)
#
# file path = D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data

# %%
import pandas as pd

# %%
df = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\Flavors.csv")

# %%
df

# %%
numeric_cols = ["Flavor Rating","Texture Rating","Total Rating"]
string_cols = ["Flavor","Base Flavor","Liked"]

# %%

# %%
# 1. Basic Group by function
# flavour is unique

# %%
df.groupby('Base Flavor')

# %%
group_by_frame = df.groupby('Base Flavor')

# %%

# %%
#2 Different aggregations using group by 

# %%
#2.1 mean()

# %%
group_by_frame.mean()  # This gave me error, stating : TypeError: Could not convert string 'ChocolateRocky RoadChocolte Fudge Brownie' to numeric
# in video, automatically only numverica values were considered

# %%
#2.1.1 - using selective or muliple columns 

# %%
group_by_frame.mean('Flavor Rating')  # picked only numerical

# %%
group_by_frame.mean(['Flavor Rating','Texture Rating','Total Rating'])   # multiple numerical

# %%
group_by_frame.mean(numeric_cols)

# %%
# 2.2 Count
df.groupby('Base Flavor').count()

# %%
#2.3 min

df.groupby('Base Flavor').min()   # this can be used for string and numbers 

# %%
# 2.4 max

df.groupby('Base Flavor').max() 

# %%
# 2.5 sum

df.groupby('Base Flavor').sum()   # for strings its concatenates 
# in video for sum only numercial values got considered. Could be a difference in python version

# %%

# %%
#3. Aggregation function 

# %%
# agg - is a dictionary. onl which columns what are the aggregations that need to be performed.

# %%
df.groupby('Base Flavor').agg({'Flavor Rating':['mean','max','count','sum']})

# %%
# 3.1 - Aggregate on more than one columns. Utilize the dictionary

# %%
df.groupby('Base Flavor').agg({'Flavor Rating':['mean','max','count','sum'], 'Texture Rating':['mean','max','count','sum']})

# %%
df

# %%
# 4. Group by on Mutile columns : Base Flavor and Like

# %%
df.groupby(['Base Flavor','Liked'])

# %%
df.groupby(['Base Flavor','Liked']).min()

# %%

# %%
#5. Get basic overview of group byu values
# using describe

# %%
df.groupby('Base Flavor').describe()

# %%
df.groupby(['Base Flavor','Liked']).describe()
# its gives values like  : count	mean	std	min	25%	50%	75%	max

# %%
# 5.1 Describe one column

# %%
df.groupby(['Base Flavor','Liked'])['Flavor Rating'].describe()

# %%
# 5.2 Describe specific columns

# %%
df.groupby(['Base Flavor','Liked'])[['Flavor Rating','Texture Rating']].describe()

# %%
