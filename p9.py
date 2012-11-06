def is_pythagorean(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	else:
		return False

def gen_triplets(sigma):
	for a in xrange(1,sigma+1):
		for b in xrange(1,sigma-a+1):
			yield (a,b,1000-a-b)

def find_pythagorean_triplet(sigma):
	for trip in gen_triplets(sigma):
		if is_pythagorean(*trip):
			return trip

