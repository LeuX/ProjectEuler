from math import ceil, floor, log10, pow
from itertools import product

def is_palindromic(number):
	def rec(remaining,num):
		if remaining == 1: return True
		if remaining == 2: return num%10==num/10
		if num/(10**(remaining-1))==num%10:
			return rec(remaining-2,(num%(10**(remaining-1)))/10)
		else: return False
	num_digits = (int(ceil(log10(number))) if number>0 else 1)
	return rec(num_digits,number)

def descend_product(maxval,minval):
	### doesn't work correctly
	""" a generator that yields tuples of numbers between
	maxval and minval. 
	The tuples are sorted decreasingly by their product. 
	
	Picture the tuples being set out on a diamond-shaped grid. 
	At the top we have (maxval,maxval). then, for every step 
	to the lower right we decrement the right value, for every 
	step to the lower left, the left value is decremented
	Since products are commutative, the left half of the diamond 
	can be ignored.
	For maxval==9 the remaining half would look like:

	9,9
	   9,8
	8,8   9,7
	   8,7   9,6
  7,7   8,6   9,5
	   7,6   8,5   9,4
	6,6   7,5   8,4   9,3
	   6,5   7,4   8,3   9,2
	5,5   6,4   7,3   8,2   9,1
	   5,4   6,3   7,2   8,1
	4,4   5,3   6,2   7,1
	   4,3   5,2   6,1
	3,3   4,2   5,1
	   3,2   4,1
  2,2   3,1
	   2,1
	1,1

	Comparing to tuples from the above chart we can see that ones
	product is bigger than the others if the one is above the other, 
	or, if both are in the same line, if the one is left of the other.
	Therefore the shape above has to be descended line by line, 
	left to right.
	"""
	def drift_apart(left, right):
		for diff in xrange(maxval - i + 1):
			a = left + diff
			b = right - diff
			if b < minval:
				break
			print a,b,a*b

	for i in xrange(maxval,minval-1,-1):
		#first the line where both left and right 
		#start with the same value
		left,right = i,i
		drift_apart(left,right)
		print	
		#then the line below, right = left - 1
		left = i
		right = i - 1
		drift_apart(left,right)
		
		print	
			 

def first_palindrome(supremum):
	return max([a*b for a,b in product(range(supremum),range(supremum)) if is_palindromic(a*b)])
