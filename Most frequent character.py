#!/usr/bin/env python
# coding: utf-8

# In[31]:


x = input('Please enter a string : ')
def most_frequent(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

a= (most_frequent(x))

sorted_dict = {}
sorted_keys = sorted(a, key=a.get,reverse=True)  

for w in sorted_keys:
    sorted_dict[w] = a[w]
    
print(sorted_dict)


# In[ ]:




