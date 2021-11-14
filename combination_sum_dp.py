#dynamic programming approach to find total number of ways to find possible patterns to form n out of given states

def sum_p(n):
	if n < 0:
	 	return 0
	elif n is 0:
		return 1

	return(sum_p(n-1)+sum_p(n-3)+sum_p(n-5))


n=7
s1=0
s1=sum_p(n)

print(s1)