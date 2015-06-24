total = 0
prev = 1
curr = 2
while curr<4000000:
	if(curr % 2 == 0):
		total += curr
	temp = curr
	curr += prev
	prev = temp

print total