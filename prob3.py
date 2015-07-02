import math

def largest_prime(n):
	factors = [1]
	sqrt = int(math.sqrt(n))
	print sqrt

	for i in range(2,sqrt):
		if(n % i == 0):
			factors.append(i)
			n = int(n/i)

	return factors[-1]

print largest_prime(600851475143)