def gen_triangles():
	counter = 1
	num = 0
	while True:
		num += counter
		counter += 1
		yield num

def find_factors(n):
	factors = []
	for i in xrange(1, n+1):
		if n % i == 0:
			factors.append(i)
	return factors

#takes forever
def find_first_triangle_with_gt_n_divisors(n):
	for i in gen_triangles():
		if len(find_factors(i)) > n:
			return i
		
