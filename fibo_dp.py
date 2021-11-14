# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    #Table to store results of subproblems
    fibo =[0]*(n+1)
 
    # Initialize first two values in table
    fibo[0] = 1
    if n != 0:
        fibo[1] = 1
        
    for i in range(2,n+1):
        fibo[i]+=fibo[i-1]+fibo[i-2]
    
    return fibo[n-1]

 
# Driver Program
 
print(Fibonacci(8))
 
