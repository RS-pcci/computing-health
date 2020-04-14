#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

DATA_PATH = 'T:/COVID/CensusMatrix/Data'
file = pd.read_excel(DATA_PATH + '/CensusMatrix.xlsx')


# In[2]:


df = file[['Floor', 'ICU', 'DEATH', 'Pred_Severe', 'Pred_Mod', 'Pred_Low']].dropna()


# In[3]:


df_copy1 = df.copy()


# In[4]:


df_copy2 = df.copy()


# In[5]:


df_copy3 = df.copy()


# In[6]:


for i in range(0, 68):
    temp = df['Pred_Low'][i]* df[['Floor', 'ICU', 'DEATH']]
    zeros_df = pd.DataFrame()
    for j in range(0, i):
        temp_zeros = pd.DataFrame(np.zeros((1,3)))
        zeros_df = pd.concat([zeros_df, temp_zeros], axis = 0)
    zeros_df = zeros_df.rename(columns = {0:'Floor',1:'ICU',2:'DEATH'})
    temp = pd.concat([zeros_df,temp], axis = 0).reset_index(drop='True').rename(columns = {'Floor': 'Floor_'+str(i+1),'ICU': 'ICU_'+str(i+1),'DEATH': 'DEATH_'+str(i+1)})

    df_copy1 = pd.concat([df_copy1, temp],axis = 1 , sort = False)

for each in (['Floor', 'ICU', 'DEATH']):
    temp = 0
    for i in range(0, 68):
        temp = temp + df_copy1[each+'_'+str(i+1)].fillna(0)
        #temp = [round(k) for k in temp]
        #print(temp)
        df_copy1['SUM_LOW_'+each] = temp
    df_copy1['SUM_LOW_'+each] = [round(k) for k in  df_copy1['SUM_LOW_'+each]]


# In[7]:


Census_Low = df_copy1[['SUM_LOW_Floor', 'SUM_LOW_ICU', 'SUM_LOW_DEATH']]


# In[8]:


for i in range(0, 68):
    temp = df['Pred_Mod'][i]* df[['Floor', 'ICU', 'DEATH']]
    zeros_df = pd.DataFrame()
    for j in range(0, i):
        temp_zeros = pd.DataFrame(np.zeros((1,3)))
        zeros_df = pd.concat([zeros_df, temp_zeros], axis = 0)
    zeros_df = zeros_df.rename(columns = {0:'Floor',1:'ICU',2:'DEATH'})
    temp = pd.concat([zeros_df,temp], axis = 0).reset_index(drop='True').rename(columns = {'Floor': 'Floor_'+str(i+1),'ICU': 'ICU_'+str(i+1),'DEATH': 'DEATH_'+str(i+1)})

    df_copy2 = pd.concat([df_copy2, temp],axis = 1 , sort = False)

for each in (['Floor', 'ICU', 'DEATH']):
    temp = 0
    for i in range(0, 68):
        temp = temp + df_copy2[each+'_'+str(i+1)].fillna(0)
        #temp = [round(k) for k in temp]
        #print(temp)
        df_copy2['SUM_Mod_'+each] = temp
    df_copy2 ['SUM_Mod_'+each] = [round(k) for k in  df_copy2['SUM_Mod_'+each]]


# In[9]:


Census_Mod = df_copy2[['SUM_Mod_Floor', 'SUM_Mod_ICU', 'SUM_Mod_DEATH']]


# In[10]:


for i in range(0, 68):
    temp = df['Pred_Severe'][i]* df[['Floor', 'ICU', 'DEATH']]
    zeros_df = pd.DataFrame()
    for j in range(0, i):
        temp_zeros = pd.DataFrame(np.zeros((1,3)))
        zeros_df = pd.concat([zeros_df, temp_zeros], axis = 0)
    zeros_df = zeros_df.rename(columns = {0:'Floor',1:'ICU',2:'DEATH'})
    temp = pd.concat([zeros_df,temp], axis = 0).reset_index(drop='True').rename(columns = {'Floor': 'Floor_'+str(i+1),'ICU': 'ICU_'+str(i+1),'DEATH': 'DEATH_'+str(i+1)})

    df_copy3 = pd.concat([df_copy3, temp],axis = 1 , sort = False)

for each in (['Floor', 'ICU', 'DEATH']):
    temp = 0
    for i in range(0, 68):
        temp = temp + df_copy3[each+'_'+str(i+1)].fillna(0)
        #temp = [round(k) for k in temp]
        #print(temp)
        df_copy3['SUM_Severe_'+each] = temp
    df_copy3['SUM_Severe_'+each] = [round(k) for k in  df_copy3['SUM_Severe_'+each]]


# In[11]:


Census_Severe = df_copy3[['SUM_Severe_Floor', 'SUM_Severe_ICU', 'SUM_Severe_DEATH']]


# In[12]:


CensusCalc =  pd.concat([df, Census_Severe, Census_Mod, Census_Low],axis = 1 , sort = False)


# In[13]:


CensusCalc


# In[14]:


CensusCalc.to_excel(r'T:\COVID\CensusMatrix\Apr7\CensusCalc_Apr7.xlsx', index = False)


# In[ ]:




