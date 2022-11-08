#!/usr/bin/env python
# coding: utf-8

# In[2]:


import bs4
import requests
import pandas as pd
import re
import openpyxl as xl


# In[3]:


page = 1
title_list = []
detail_list =[]
date_list = []
while page <= 3 :
    data = requests.get('https://www.infoquest.co.th/tag/%E0%B8%AD%E0%B8%B1%E0%B8%95%E0%B8%A3%E0%B8%B2%E0%B8%A7%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%87%E0%B8%B2%E0%B8%99/page/' +str(page))
    soup = bs4.BeautifulSoup(data.text)
    for n in soup.find_all('div',{'class':'info'}):
        title_list.append(n.find('header',{'class':'entry-header'}).text.replace('\n',''))
        detail_list.append(n.find('div',{'class':'entry-summary'}).text.replace('\n',''))
        date_list.append(n.find('time',{'class':'updated'}).text)
    print('Complete page number: ',page)
    page += 1
table = pd.DataFrame([title_list,detail_list,date_list]).transpose()
table.columns = ['title','detail','date']
table.set_index('title')


# In[ ]:




