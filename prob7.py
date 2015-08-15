# Using Sieve of Eratosthenes

def primes(countn):
	p = {}
	n = 300000
	for i in range(2, n):
		p[i] = True
	i = 2
	count = 1
	
	while(count < countn):
		k = 2
		while i*k < n + 1:
			p[i*k] = False
			k += 1

		i = i + 1
		while i<n:
			if p[i] == True:
				break
			i+= 1
		count += 1
	return i, count

print primes(10001)