def is_prime(n, primes):
	for i in primes:
		if not n % i:
			return False
	return True
primes = [2, 3, 5, 7, 11, 13]
i = 15
while True:
	if is_prime(i, primes):
		primes.append(i)
	if len(primes) == 10001:
		print max(primes)
		break
	i += 1