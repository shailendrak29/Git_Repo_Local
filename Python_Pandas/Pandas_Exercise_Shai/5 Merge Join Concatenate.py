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
#
# ![image.png](attachment:cfcd305b-c408-46d2-9f02-50ff0d88e866.png)
#

# %%
# filelocation : D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data

# %%
import pandas as pd 

# %%
df1 = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\LOTR.csv")

# %%
df1

# %%
df2 = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\LOTR 2.csv")

# %%
df2

# %%
# 1. Merge - Just like join 

# %%
#1.1 df1 automatically becomes the left 

# inner join
df1.merge(df2)  #Columns names are matched automatically, i.e. FellowshipID	FirstName

# %%
df1.merge(df2, how = 'inner')

# %%
df1.merge(df2, how = 'inner',on ='FellowshipID')  # this brings FirstName from each df

# %%
df1.merge(df2, how = 'inner',on =['FellowshipID','FirstName'])   # same as default, but explicityle mentioning the columns and type of join 

# %%
df1.merge(df2, how = 'inner',on =['FellowshipID','FirstName'])   # same as default, but explicityle mentioning the columns and type of join 

# %%

# %%
#1.2 Merge - Outer

df1.merge(df2, how ='outer')

# %%
#Observations : 
# If value is not present NaN (not a Number) represents missing or undefined data. 
# overlapping data will not get duplicated 

# %%
# 1.3 Merge - left

df1.merge(df2, how ='left')

# %%
# 1.3 Merge - right

df1.merge(df2, how ='right')

# %%
# 1.4 Merge - cross

df1.merge(df2, how ='cross')

# 5x4 = 20

# %%

# %%
#2 Join
# similar to merge but mor complicated

# %%
# df1.join(df2)

# %%
df1.join(df2, on = 'FellowshipID', how ='outer', lsuffix = '_left')

# %%
df1.join(df2, on = 'FellowshipID', how ='outer', lsuffix = '_left', rsuffix = '_right')

# %%
#Observations : 
# Join is more righid, as it needs mandatory fields like on, how and either one suffix
# Join works well with indexes

# %%
# 2.1 join with index

# %%
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_left', rsuffix = '_right')

# %%
df4

# %%
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_left', rsuffix = '_right', how = 'outer')

# %%
df4

# %%
#Observation 
# Join is more rigid as compared to merge.
    # The instructor prefers merge as its easy for use

# %%

# %%
# 3. Concatenate - is like union

# %%
pd.concat([df1,df2])  # use a list of df 

# %%
# Observation : 
# NaN when value is not present

# %%
# 3.1. Concatenate - selecting only common columns, use join = inner (kind of join at column level)

pd.concat([df1,df2], join = 'inner')

# %%
# 3.2. Concatenate - selecting all columns, use join = outer

pd.concat([df1,df2], join = 'outer')

# %%
# 3.2.1 Concatenate - selecting all columns, use join = outer, with axis =0 is defaut

pd.concat([df1,df2], join = 'outer', axis =0)

# %%
# 3.2.1 Concatenate - selecting all columns, use join = outer, with axis =1 

pd.concat([df1,df2], join = 'outer', axis =1)

# %%
# Observation
# axis= 1, places the data side by side, the way merge might look 

# %%

# %%

# %%
