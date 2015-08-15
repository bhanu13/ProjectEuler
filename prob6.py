
def sumsqdiff(n):
	val = 0
	for i in range(1, n+1):
		for j in range(i+1, n+1):
			val += i*j*2
	return val

def main():
	print sumsqdiff(100)
main()