def factorize(number):
	def rec_fac(n, gen):
		try:
			prime = gen.next()
		except StopIteration:
			return []
		if n % prime == 0:
			ret = []
			while n % prime == 0:
				ret.append(prime)
				n /= prime
			return ret + rec_fac(n, gen)			
		else:
			return rec_fac(n, gen)

	sieve = gen_primes(number)
	return rec_fac(number, sieve)

def gen_primes(supremum):
	sieve = [0,0,]+(range(2,supremum+1))
	for factor in sieve:
		if factor == 0:
			continue
		for i in xrange(supremum / factor + 1):
			sieve[factor * i]=0
		yield factor
			
#this code is ugly
def factorize_bignum(num):
	def is_prime(n):
		for i in xrange(2,num):
			if num % i == 0:
				return False
		return True

	if num == 1:
		return []
	else:
		if is_prime(num):
			return [num]
		else:
			for i in xrange(2,num):
				if num % i == 0:
					return factorize_bignum(i) + factorize_bignum(num/i)
