from p3 import factorize
from copy import copy
from itertools import groupby

def least_common_multiple(*args):
	factors={}
	for num in args:
		# prime factor tuples of both values, (prime, count)
		factors[num] = [(k, len(list(g))) for k,g in groupby(factorize(num))]
	
	primes = {}
	for num in iter(factors):
		for prime,count in factors[num]:
			primes.setdefault(prime,[]).append(count)
	
	lcm = 1
	for prime in iter(primes):
		lcm *= prime ** (max(primes[prime]))
	
	return lcm
