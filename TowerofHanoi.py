
#Create a condition on x1, x2 and x where print True if x is on the line joining x1 and x2\n",
def compare(x1,x2,x):
    if((x1<=x and x2>=x) or (x2<=x and x1>=x)):
        print(x,"true point lies on line",x1,x2)
    else:
       print(x,"false point doesn't lies on line",x1,x2)

compare(1,-1,0)
compare(-5,-6,1)
compare(4,8,6)
compare(-3,3,-1)
compare(0,0,0)
compare(1,0,-1)

#Q: Two lines x1 --> x2 and x3 --> x4, print True, if overlapping or touching otherwise print False\n",

def pointonline(x1,x2,x):
    if((x1<=x and x2>=x) or (x2<=x and x1>=x)):
       return bool(True)
    else:
     return bool(False)
       
def overlap(x1,x2,x3,x4):
  if(pointonline(x1,x2,x3) or pointonline(x1,x2,x4) or pointonline(x3,x4,x1) or pointonline(x3,x4,x2)):
          print("True lines",x1,x2 ," touch or overlap", x3,x4)
  else:
     print("False lines",x1,x2," don't overlap ", x3,x4)      

overlap(1,2,2,-5)
overlap(2,1,2,5)
overlap(1,3,2,5)
overlap(1,-3,0,5)
overlap(3,-3,1,-5)
overlap(1,3,4,5)
overlap(-2,-4,2,5)


