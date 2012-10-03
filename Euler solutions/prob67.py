#Result is 
lines = open("triangle67.txt").read().splitlines()
numbers = {}
i = 0
for line in lines:
	numbers[i] = []
	for c in line.split(" "): numbers[i].append(int(c))
	i += 1
for y in reversed(range(0, 99)):
	for x in range(0, y+1):
		if numbers[y+1][x] > numbers[y+1][x+1]: numbers[y][x] += numbers[y+1][x]
		else: numbers[y][x] += numbers[y+1][x+1]
print numbers[0][0]