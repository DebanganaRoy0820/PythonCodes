# Python code to demonstrate naive
# method to compute gcd ( recursion )
#doesn't depend on which is bigger number
  
def hcfnaive(a,b):
    if a>b:
        t=1
    else:
        t=a
        a=b
        b=t
    
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
  
a = 48
b= 60
g=hcfnaive(a,b)
  
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (g)