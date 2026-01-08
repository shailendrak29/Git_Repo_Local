#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Youtube link : https://www.youtube.com/watch?v=Mdq1WWSdUtw&t=1347s


# In[1]:


# file_path = D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data


# In[24]:


import pandas as pd


# In[ ]:


# 1. Read CSV


# In[3]:


pd.read_csv("D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv")


# In[5]:


#r - reads the file path as raw text 
# without r also my jupyter worked. in video it showed unicode error


# In[6]:


pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv")
# header populated automatically
#index shown automatically
# shift+Tab : This gives options about the command


# In[8]:


pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv", header = 1)  # picks first data as header
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv", header = None)  # Makes header as 0 and 1, similar to row index.


# In[13]:


# can assign a new name to the Columns using names 
# header can be None, 0, 1 , irrespective of the name . it will behave as it is
pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv", header = 0, names =['Country','Region'] )  # Makes header as 0 and 1, similar to row index.


# In[14]:


df = pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.csv")


# In[16]:


df


# In[ ]:





# In[17]:


#2. Read txt


# In[19]:


pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.txt")


# In[20]:


pd.read_csv(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.txt",sep ='\t')


# In[23]:


#better way is to read_table , works with and without separator

pd.read_table(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\countries of the world.txt")


# In[ ]:





# In[26]:


# 3. Read JSON 


# In[44]:


pd.read_json(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\json_sample.json")


# In[ ]:





# In[28]:


# 4.Read Excel files 


# In[31]:


pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx")

# by default it reads the first sheet 


# In[33]:


pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')

# by default it reads the first sheet 
# Proving the Sheet_name allows us to pick the required sheet


# In[42]:


# to see all the values in the dataframe

pd.set_option('display.max.rows',235)
pd.set_option('display.max.columns',40) # columns created bottom seek bar for json file, but for excle it did not create bottom seek bar 


# In[36]:


pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')


# In[43]:


pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx")


# In[45]:


# 5. checking insights about the dataframe


# In[46]:


df = pd.read_excel(r"D:\Shailendra Kelkar\Projects\My_Git_Repo\Python_Pandas\PandasYouTubeSeries-data\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')


# In[47]:


df.info()


# In[48]:


df.shape


# In[49]:


df.head(10)


# In[50]:


df.tail(10)


# In[52]:


df['Rank'].tail(10)  #no dot bertween rank and df


# In[55]:


# using indexes of rows
# loc -- looks for the string information
# iloc -- looks for integer value
# useful while changing the index


# In[56]:


df.loc[224]


# In[57]:


df.iloc[224]


# In[58]:


df.loc['Uzbekistan']  # this will work when the index is changed to Country


# In[ ]:




