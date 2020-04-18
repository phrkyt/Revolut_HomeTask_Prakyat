
# coding: utf-8

# # Revolut Home Task

# In[25]:


import numpy as np 
import pandas as pnd
import scipy as sp 
import matplotlib.pyplot as plt #data visualisation
import seaborn as sb
import json
import ast


# ### Load and Format Data

# In[88]:


docrep=pnd.read_csv("C:\Revolut_Challenge_Prakhyath\doc_reports_sample.csv")


# In[3]:


facerep=pnd.read_csv("C:\Revolut_Challenge_Prakhyath\\face_reports_sample.csv")


# In[4]:


docrep.head()


# In[5]:


facerep.head()


# In[90]:


propdf=docrep[['user_id','attempt_id','properties']]


# In[ ]:


for index, row in propdf.iterrows():
    #print(type(row['properties']))
    dict=ast.literal_eval(row['properties'])
    #print(type(dict))
    #print(dict)
    for key in dict:
        propdf.loc[index,key]=dict[key]


# In[87]:


propdf=propdf.drop(columns=['gender','document_type','date_of_expiry','issuing_country','nationality','issuing_date','issuing_state','document_version'])


# In[75]:


docrep = pnd.merge(docrep, propdf, on='attempt_id')


# In[ ]:


docrep.head()


# In[89]:


docrep.shape


# In[85]:


for index, row in propdf.iterrows():
    print(index)
    print(propdf.loc[index,'gender'])
    break;


# In[ ]:


propdf.head()

