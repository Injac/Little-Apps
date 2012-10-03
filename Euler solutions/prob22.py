names = open("names.txt").read().replace("\"", "").split(",")
names.sort()
total = 0
for i in range(0, len(names)): total += (i + 1) * sum([ord(char) - 96 for char in names[i].lower()])
print total