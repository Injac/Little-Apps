#Result is 21124
def wordIt(num):
	s = ""
	units = num%10
	if units >= 10: units -= 10
	tens = ((num%100)-(num%10))/10
	if tens >= 10: tens -= 10
	hundreds = (num-(num%100))/100
	if hundreds >= 10: hundreds -= 10
	thousands = (num-(num%1000))/1000
	if thousands >= 10: thousands -= 10
	nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	tenN = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	if thousands: s+= nums[thousands-1] + "thousand"
	if hundreds: s+= nums[hundreds-1] + "hundred"
	if (tens or units) and hundreds: s+= "and"
	if tens == 1:
		teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
		s += teens[units]
	else:
		if tens: s += tenN[tens-1]
		if units: s += nums[units-1]
	return s
string = ""
for i in range(1, 1001): string += wordIt(i)
print len(string)
	