#!/usr/bin/env python
# coding: utf-8

# In[31]:


from dsmlibrary.datanode import DataNode
dir_raw_id = 66
datanode = DataNode()
datanode.upload_file(directory_id=dir_raw_id, file_path='ข่าวว่างงาน.csv')


# In[1]:


from dsmlibrary.datanode import DataNode
import json
from tqdm.auto import tqdm
import pandas as pd


# In[ ]:


dir_raw_id = 66
dir_process_id = 67


# In[ ]:


datanode = DataNode()


# In[ ]:


meta, fp = datanode.get_file(datanode.get_file_id(directory_id=dir_raw_id, name='ข่าวว่างงาน.csv'))
meta


# In[ ]:


data = pd.read_csv('ข่าวว่างงาน.csv')
data

