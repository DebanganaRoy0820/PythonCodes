
def leftRotate(arr,d,n):
	for i in range(d):
		leftRotatebyOne(arr,n)


def leftRotatebyOne(arr,n):
	t1=arr[0]
	for i in range(n-1):
		arr[i]=arr[i+1]
	arr[n-1]=t1


import array
arr = array.array('i',[1,2,3,4,5,6,7])
d=2
print ("The new created array is : ",end=" ")
for i in range (0, len(arr)):
	    print (arr[i], end=" ")
leftRotate(arr,d,len(arr))
print ("The new created array is : ",end=" ")
for i in range (0, len(arr)):
	    print (arr[i], end=" ")

