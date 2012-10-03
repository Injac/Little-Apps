def getFactors(num):
	fctrs = []
	for i in range(1, num/2+1):
		if num % i == 0:
			if i not in fctrs:fctrs.append(i)
	fctrs.append(num)
	return fctrs

file = file("triangles4.txt", "w")
for i in range(1, 500):
	fctrs = getFactors((i*(i+1))/2)
	file.write(str(i) + ":" + str((i*(i+1))/2) + ":" + str(len(fctrs)) + "\n")
print "Done"