#!/usr/bin/env python
# coding: utf-8

# # Drawing Conclusions Quiz
# Use the space below to explore `store_data.csv` to answer the quiz questions below.

# In[2]:


# imports and load data
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('store_data.csv')


# In[3]:


# explore data
df.describe()


# In[7]:


df.tail()


# In[19]:


# total sales for the last month
df.iloc[196:200, 1:6].sum()


# In[20]:


# average sales
df['storeA'].mean()


# In[21]:


df['storeB'].mean()


# In[22]:


df['storeC'].mean()


# In[23]:


df['storeC'].mean()


# In[24]:


df.mean()


# In[27]:


# sales on march 13, 2016
df.query('week == "2016-03-13"')


# In[41]:


# worst week for store C
df[df['storeC'] == df['storeC'].min()]


# In[42]:


# total sales during most recent 3 month period
df.tail(20)


# In[45]:


last3months = df.query('week >= "2017-12-03"')


# In[46]:


last3months.sum()

