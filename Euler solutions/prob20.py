#Result is 648
def bang(num):
	r = 1
	for i in range(1, num+1): r *= i
	return r
t = 0
for i in str(bang(100)): t += int(i)
print t