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

# %% [markdown] editable=true slideshow={"slide_type": ""}
# ## Indexing
#
# [Youtube link](https://www.youtube.com/watch?v=Mdq1WWSdUtw&t=1347s)
#
# [Introduction to Markdown](https://www.youtube.com/watch?v=6dtnmERmQoI&t=115s)
#
# file_path = D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data

# %%
import pandas as pd

# %%
df = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population.csv")

# %%
df

# %%

# %%
# There multiple ways of creating Index

# %%
#1. Create index while creating df itself in read_csv

# %%
df = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population.csv", index_col = "Country")

# %%
df

# %%
#2. Resetting the Index 

# %%
df.reset_index(inplace=True)

# %%
df

# %%
#3. Basic setting index for a df
df.set_index('Country')  # this does not change the df itself

# %%
# 3.1 How to reset the index ?

# %%
df.set_index('Country', inplace = True)  #inplace = True , applies the index to df itself. else we need to create a new df

# once a columns is marked as Index it does not remain a column. try setting index twice on same column to see the error

# %%
df

# %%

# %%
# 4. Searching using Index 
# loc , iloc

# %%
df.loc['Albania']

# %%
df.iloc[1]

# %%

# %%
# 5. Multi Indexing
# Create multiple indexes

# %%
df.reset_index(inplace=True)

# %%
df

# %%
df.set_index(['Continent','Country'], inplace=True)

# %%
df

# %%

# %%
# 6. Sort index

# %%
df.sort_index()
# 

# %%
pd.set_option('display.max.rows',235)

# %%
df.sort_index(ascending=[True])  #by default its True 

# %%
df.sort_index(ascending=[True,False])  # to set the second index as descending

# %%

# %%
# 7. Search using Multiple Index 
# loc, iloc

# %%
df.loc['Africa']

# %%
df.loc['Africa','Angola']

# %%
# df.loc['Angola']   # only country gives error as it is composed of Continent and Country

# %%
df.iloc[1]   # this still remains as it is based on its initial index. This is rock solid.

# %%
