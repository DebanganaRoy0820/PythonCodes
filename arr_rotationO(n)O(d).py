import array
arr = array.array('i',[1,2,3,4,5,6,7])
d=2
print ("The new created array is : ",end=" ")
for i in range (0, len(arr)):
	    print (arr[i], end=" ")
temp = array.array('i')
temp.insert(0,arr[0])
temp.insert(1,arr[1])
for i in range(len(arr)-d):
	arr[i]=arr[i+d]
print('\r')
j=0
for i in range((len(arr)-d),len(arr)):
	arr[i]=temp[j]
	j=j+1
print ("The new created array is : ",end=" ")
for i in range (0, len(arr)):
	    print (arr[i], end=" ")