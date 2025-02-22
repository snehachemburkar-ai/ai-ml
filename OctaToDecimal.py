#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 2. Convert base 8 base 10 for 4 digit number
x=5942
base=8


# In[15]:


d0=x%10
print(d0)


# In[16]:


x = x // 10
print(x)
d1=x%10
print(d1)


# In[17]:


x=x//10
d2=x%10
print(d2)


# In[18]:


x=x//10
d3=x%10
print(d3)


# In[21]:


convert=d0*1+d1*8+d2*8*8+d3*8*8*8
print(convert)


# In[46]:


import math
number=4623
base=8
result=0
for x in range(4):
   digit=number%10
   print("digit:",digit)
   number=number//10
  # print("number:",number)
   #print("x:",x)
   result=result+digit*(math.pow(base,x))
print("Result=", result)


# In[ ]:




