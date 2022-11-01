#!/usr/bin/env python
# coding: utf-8

# ## read stored data from DataPlatform

# In[ ]:


from dsmlibrary.datanode import DataNode
dir_raw_id = 66
datanode = DataNode()
datanode.upload_file(directory_id=dir_raw_id, file_path='../DataNews.csv')


# In[ ]:


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


meta, fp = datanode.get_file(datanode.get_file_id(directory_id=dir_raw_id, name='DataNews.csv'))
meta


# In[ ]:


data = pd.read_csv('../DataNews.csv')
data


# ## write DataNode to DataPlatform

# In[ ]:


datanode.write(df=data, directory=dir_process_id, name="Crime-News", profiling=True, lineage=[datanode.get_file_id(directory_id=dir_raw_id, name='DataNews.csv')])

