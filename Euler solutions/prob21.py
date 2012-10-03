#Result is 40284
divs = [0] * 10000
def calcSum(num):
	t = 0
	for i in range(1, (num/2)+1):
		if num % i == 0: t += i
	return t
for i in range(1, 10000): divs[i] = calcSum(i)
sum = 0
for i in range(1, 10000):
	if divs[i] < 10000:
		if i == divs[divs[i]] and i != divs[i]:
			sum += i
print sum