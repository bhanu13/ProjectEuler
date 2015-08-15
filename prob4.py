def CheckPalin(n):
	if len(n) == 0 or len(n) == 1:
		return True
	return (n[0] == n[-1] and CheckPalin(n[1:-1]))

def FindLargest():
	n = 0

	for i in range(100, 1000):
		for j in range(i, 1000):		
			if(CheckPalin(str(i*j)) and i*j > n):
				n = i*j

	return n

print FindLargest()