import math

# Create a List of primes less than 20
def primes(n):
	p = {}
	for i in range(2, n+1):
		p[i] = True
	# print p
	i = 2
	while(i<math.sqrt(n+1)):
		k = 2
		while i*k < n + 1:
			p[i*k] = False
			k += 1

		j = i + 1
		while j<n:
			if p[j] == True:
				break
			j+= 1
		i = j

	return p
			
# For all primes find the max frequency of each prime
def factors(n, p):
	f = {}
	for i in p:
		f[i] = 1

	for i in range(2, n):
		if i not in p:
			for j in p:
				if j > i:
					break
				count = 0
				temp = i
				while temp % j == 0:
					count += 1
					temp /= j
				if f[j] < count:
					f[j] = count
	return f

def main():
	firstprimes = primes(20)
	p = list()
	for k in firstprimes:
		if firstprimes[k]:
			p.append(k)
	val = 1			# val is the greatest common multiple
	f = factors(20, p)
	for i in f:
		val = val * math.pow(i, f[i])

	print val
main()