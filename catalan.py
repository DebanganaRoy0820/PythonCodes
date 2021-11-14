def catalan(n):
	if n <= 1:
		return 1
	
	s=0
	for i in range(n):
		s+= catalan(n-i-1)*catalan(i)
	return s


print(catalan(5))