from p3 import gen_primes

def sum_primes(maximum):
	ret = 0
	for prime in gen_primes(maximum):
		ret += prime
	return ret
