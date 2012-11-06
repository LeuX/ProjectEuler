from p3 import gen_primes

def n_th_prime(n):
	primes = []
	counter = n
	while len(primes) < n-1:
		print counter
		counter *= 10
		primes = list(gen_primes(counter))
	return primes[n-1]
