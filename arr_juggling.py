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

def leftRotate(arr,d,n):
	g=hcfnaive(d,n)
	print(g)
	for i in range(g):
		temp = arr[i]
		j=i
		while True:
			k = j + d
			if k >= n:
				k = k - n
			if k == i:
		   		break

			arr[j] = arr[k]
			j = k
			arr[j] = temp


import array
arr = array.array('i',[1,2,3,4,5,6,7,8,9,10,11,12])
d=3
n=len(arr)
print ("The new created array is : ",end=" ")
for i in range (0, n):
	    print (arr[i], end=" ")
leftRotate(arr,d,len(arr))
print ("The new created array is : ",end=" ")
for i in range (0, n):
	    print (arr[i], end=" ")
