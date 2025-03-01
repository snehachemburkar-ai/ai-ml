#!/usr/bin/env python
# coding: utf-8


# # 2. Convert base 13 to base 10 for 4 digit number
x=5949
base=13
print("base:",base)
d0=x%10
print(d0)
x = x // 10
print(x)
d1=x%10
print(d1)
x=x//10
d2=x%10
print(d2)

x=x//10
d3=x%10
print(d3)


convert=d0*1+d1*13+d2*13*13+d3*13*13*13
print("Coverted number B(13)",x," to decimal",convert)

# 2. Convert base 13 to base 10 for 4 digit number

import math
number=4629
base=13
result=0
print("base:",base)
for x in range(4):
   digit=number%10
   #print("digit:",digit)
   number=number//10
  # print("number:",number)
   #print("x:",x)
   result=result+digit*(math.pow(base,x))
print("Converted base(13) to decimal =", result)


#    ##Function base conversion

# 
# 2. Convert base 13 to base 10 for 4 digit number with alphabets

import math
base=13
print("base: ",base)


def findnum(num):
     if(num=='A'):
        num=10
     elif(num=='B'):
         num=11
     else:
         num=12
     return num
     
def converBase13toDecimal(number):
        global digit
        global result
        global base
        global i
        i=0
        result=0
        numlen =len(number)
        #print("Number Length: ",numlen)
        while(numlen>=1):
           digit=number[numlen-1]
           if((digit=='A') or (digit=='B') or (digit=='C')):
                 num=findnum(digit)
           else:
               num=int(digit)
           #print("Number in int : ",num)
           result=result+num*(math.pow(base,i))
           #print(result)
           numlen=numlen-1
           i=i+1
        print("Converted base(13): ", number," to decimal =", int(result))
        return(result)



converBase13toDecimal('10')
converBase13toDecimal('20')
converBase13toDecimal('30')
converBase13toDecimal('100')
converBase13toDecimal('46AC')




