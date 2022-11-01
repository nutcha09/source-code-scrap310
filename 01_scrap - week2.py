#!/usr/bin/env python
# coding: utf-8

# In[3]:


import bs4
import requests
import pandas as pd
import re
import openpyxl as xl


# In[4]:


page = 1
topic_list = []
descrip_list = []
while page <= 29 :
    data = requests.get('https://www.bbc.co.uk/search?q=crime+thailand&page=' + str(page))
    soup = bs4.BeautifulSoup(data.text)
    for n in soup.find_all('div',{'class':'ssrcss-dirbxo-PromoSwitchLayoutAtBreakpoints e3z3r3u0'}):
        topic_list.append(n.find('div',{'class':'ssrcss-1f3bvyz-Stack e1y4nx260'}).find('span',{'role':'text'}).text)
        descrip_list.append(n.find('p',{'class':'ssrcss-1q0x1qg-Paragraph eq5iqo00'}).text)
    print('Complete page number: ',page)
    page += 1
table = pd.DataFrame([topic_list,descrip_list]).transpose()
table.columns = ['topic','descrip']
table.set_index('topic')


# In[ ]:




