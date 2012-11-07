def cross_total(n):
	if n < 10: return n
	else:	return n % 10 + cross_total(n/10)


