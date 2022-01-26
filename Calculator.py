#!/usr/bin/env python
# coding: utf-8

# In[3]:


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2
    
def divide(n1,n2):
    return n1/n2

print('''
      1: Add
      2: Subtract
      3: Multiply
      4: Divide ''')

i = int(input('Choose an option(1,2,3,4) :'))
      
Num1 = float(input('Choose 1st number :'))    
Num2 = float(input('Choose 2nd number :'))      

if i == 1:
      print(add(Num1,Num2))
elif i == 2:
      print(subtract(Num1,Num2))
elif i == 3:
      print(multiply(Num1,Num2))
elif i == 4:
      print(divide(Num1,Num2))  
else:
    print('Invalid output')
    


# In[ ]:




