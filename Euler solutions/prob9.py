#Result is 31875000
import math
for a in range(1, 1000):
	for b in range(a, 1000):
		if a+b+math.sqrt((a*a)+(b*b)) == 1000:
				print str(a) + "*" + str(b) + "*" + str(math.sqrt((a*a)+(b*b))) + "=" + str(a*b*math.sqrt((a*a)+(b*b)))