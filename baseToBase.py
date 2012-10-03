#Usage is baseToBase("100", "0123456789", "01")
#New base could be anything like 01 to do binary, 0123456789 to do decimal
#Or 0123456789AB for duodecimal or even 0123456789abcdef for hex

def baseToBase(originalNumber, originalBase, newBase):
	numberAsInteger = 0
	for n in range(0, len(originalNumber)):
		numberAsInteger = (numberAsInteger * len(originalBase)) + int(originalBase[originalBase.find(originalNumber[n])])
	newNumber = ""
	if (numberAsInteger == 0): newNumber = "0"
	else:
		while (numberAsInteger > 0):
			newNumber = newBase[numberAsInteger % len(newBase)] + newNumber
			numberAsInteger = (numberAsInteger - numberAsInteger % len(newBase)) / len(newBase)
	return newNumber