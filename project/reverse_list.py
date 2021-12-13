#!/usr/bin/env python
# coding: utf-8

# In[22]:


l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


# In[24]:


def reverse_list(l):
    for x in l:
        x.sort(reverse=True)
    return l


# In[25]:


reverse_list(l)


# In[ ]:




