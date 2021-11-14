#dynamic programming approach to find total number of ways to find possible patterns to form n out of given states	
#print the possible patterns


def sum_p(n):
	i=0
	lookup=[0]*(n+1)
	if n < 0:
	 	return 0
	elif n is 0:
		return 1

	if n not in lookup:
		# Taking input key = 1, value = Geek
		lookup[n]= lookup[n-1]+lookup[n-3]+lookup[n-5]
		#i+=1

	return lookup
  
# Main Function 
 
n=7
print(sum_p(7))

