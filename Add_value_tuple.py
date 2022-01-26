#!/usr/bin/env python
# coding: utf-8

# ### Add values to a tuple
# 

# In[1]:


x = ('a','b','c')

newvalue = 'd'
newvalue_tuple = (newvalue,)
final_tuple = x + newvalue_tuple
print(final_tuple)


# ### Incrementing values by 2 in the range instead of 1

# In[2]:


for i in range(0,10,2):
    print(i)


# ### Infinite for loop

# In[ ]:


def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1

for x in zero_to_infinity():
    print(x)


# In[ ]:




