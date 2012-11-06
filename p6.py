from itertools import imap

def sumsquares(num):
	return sum(imap(lambda x : x*x, xrange(num+1)))

def squaresum(num):
	return sum(range(num+1))**2


