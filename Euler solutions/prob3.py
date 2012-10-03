#Result is 6857

num = 600851475143L
factors = str(num) + "="
quit = 0
while 10 == 10:
	i = 2
	while 10 == 10:
		if i == num:
			factors = factors + str(num)
			quit = 1
			break
		if num % i == 0:
			num = num / i
			factors = factors + str(i) + "*"
			break
		i = i + 1
	if quit:
		break

print "What is the largest prime factor of the number 600851475143?"
print factors
