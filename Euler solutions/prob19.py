#Result is 171
from datetime import date
from calendar import monthrange
count = 0
for y in range(1901, 2001):
	for m in range(1, 13):
		if monthrange(y, m)[0] == 6: count += 1
print count