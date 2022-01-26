#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = [10,'python',35.5,'Allen','code']


# In[2]:


x.append(98)
x.copy()


# In[3]:


y = [20,22]
x.extend(y)
print(x)


# In[4]:


x.count(20)


# In[5]:


x.index(35.5)


# In[6]:


x.insert(5,'L')
print(x)


# In[7]:


x.pop(5)


# In[9]:


x.remove('python')


# In[10]:


x.reverse()
print(x)


# In[13]:


x.clear()
print(x)


# In[ ]:




