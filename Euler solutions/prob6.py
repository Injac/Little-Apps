one = 0
two = 0
for i in range(1, 101):
	one += i*i
	two += i
two *= two
print str(two - one)