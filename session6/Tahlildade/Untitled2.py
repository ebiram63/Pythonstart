#!/usr/bin/env python
# coding: utf-8

# In[21]:


number = input("insert your number")
number = float(number)
if  0 < number < 1: 
    if number >= 0.9:
        print("A")
    else:
        if(0.9 > number >= 0.8):
            print("B")
        elif(0.8 > number >= 0.7):
            print("C")
        elif(0.7 > number >= 0.6):
            print("D") 
        elif(number > 0.6):
            print("F")  
else:             
    number = int(input("insert your number"))


# In[ ]:


0.9


# In[ ]:




