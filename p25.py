from p2 import fibgen
from math import ceil, log10

for i, fib in enumerate(fibgen(10**1001)):
	if int(ceil(log10(fib))) >= 1000:
		print i+2, fib
		break
