#Result is 1366
digits = [-1] * 1000
digits[0] = 1
def firstNegative():
	r = 0
	for d in digits:
		if d == -1: break
		r += 1
	return r

def multi():
	digits[0] *= 2
	for i in range(1, firstNegative()):
		if digits[i-1] > 10:
			digits[i] = digits[i] + digits[i] + ((digits[i-1]-(digits[i-1]%10))/10)
		else: digits[i] *= 2

def printIt():
	s = ""
	for d in digits:
		if d != -1: s = str(d) + s
		else: break
	return s

for i in range(0, 1000):
	multi()
t = 0
for s in printIt():
	t += int(s)
print t