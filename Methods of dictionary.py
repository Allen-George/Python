#!/usr/bin/env python
# coding: utf-8

# In[4]:


mydict = {'a': 10, 'b' : 12, 'c' : 5, 'd' : 20}


# In[25]:


mydict.copy()


# In[19]:


mydict.get('c')


# In[24]:


mydict.items()


# In[26]:


mydict.keys()


# In[27]:


mydict.values()


# In[32]:


mydict.pop('d')


# In[34]:


mydict.popitem
print(mydict)


# In[36]:


mydict.setdefault('a')


# In[39]:


mydict.update({'f':70,'z':55})
print(mydict)


# In[41]:


mydict.clear()
print(mydict)

