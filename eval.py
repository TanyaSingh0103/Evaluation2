#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymongo')


# In[1]:


from pymongo import MongoClient


# In[2]:


import pandas as pd


# In[4]:


client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['mycollection']


# In[7]:


df = pd.read_csv('medical.csv')

collection.insert_many(df.to_dict('records'))

print("Data inserted into MongoDB successfully.")

df_mongo = pd.DataFrame(list(collection.find()))

print("DataFrame created")
print(df_mongo.head())


# In[10]:


providers_in_ca = df[df['practicestate'] == 'CA']
print(providers_in_ca[:10])


# In[13]:


ny_providers = df[(df['practicestate'] == 'NY') & (df['specialitieslist'] == 'Medical Supply Company Other') & (df['supplieslist'] == 'OXYGEN & EQUIPMENT')]
print(ny_providers)


# In[19]:


for row in df.iterrows():
    if row[0] == '20506619':
        row[10] = '123123123'
        print(row)


# In[29]:


supplylist = df.groupby(df['supplieslist'])
print(list(supplylist)[:10])


# In[ ]:




