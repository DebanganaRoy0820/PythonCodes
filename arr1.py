#importing arrays
import array
arr = array.array('i', [1, 2, 3])
# printing original array
print ("The new created array is : ",end=" ")
for i in range (0, len(arr)):
    print (arr[i], end=" ")

print("\r")
arr.append(4)
print(arr)
arr.insert(3,8)
print("The array after insertion is")
for i in range (0, len(arr)):
    print (arr[i], end=" ")
print("The array after popping")
print(arr.pop(1))
print("The array after removing 1")
print(arr.remove(1))

print ("The index of 1st occurrence of 4 is : ",end="")
print (arr.index(4))

#print ("The index of 1st occurrence of 2 is : ",end="")
#print (arr.index(2))
#ValueError: array.index(x): x not in list

#using reverse() to reverse the array
arr.reverse()

# printing final array
print ("The final array is : ",end=" ")
for i in range (0, len(arr)):
    print (arr[i], end=" ")

