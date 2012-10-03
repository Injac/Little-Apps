#Result is 580085

max = 0

for x in range(100, 999):
	for y in range(100, 999):
		one = str(x*y)
		two = one[::-1]
		if one == two:
			if x*y > max:
				max = x*y
print "Find the largest palindrome number made from the product of two 3-digit numbers."
print max
