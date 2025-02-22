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


#    ##Function base conversion

# In[30]:





# In[ ]:



    

    


# In[93]:


#import math
#global number
#global base
#global result
#result=0
#number=4623
#for x in range(4):
 #   extractlastdigit(digit)
  #  calculate_result(x,result)
#print("Result=", result) 


# In[56]:




        


# In[35]:



def extractlastdigit():
        global digit
        global result
        global base
        global number
        global i
        print("digit: ", digit)
        print("number: ",number)
        print("i: ",i)
        digit=number % 10
        number=number // 10
        result=result+digit*(math.pow(base,i))
        print("Result=", result)
        i=i+1
        if(number==0):
             print("Final Result=", result)
        else:
            extractlastdigit() 


# In[36]:


#Recursive program 
import math
digit=1
result=0
base=8
i=1
number=4623
extractlastdigit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




