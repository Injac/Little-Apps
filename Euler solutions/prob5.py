#Result is 232792560
number = 20 * 19 * 9 * 17 * 8 * 15 * 14 * 13 * 6 * 11

i = 20
while 1:
	i = i + 20 
	ok = 1
	for x in range(1, 20):
		if i % x != 0:
			ok = 0
			break
	if ok == 1:
		number = i
		break

print "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"
print number
