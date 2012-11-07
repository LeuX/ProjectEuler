def eat1s(num):
	return {
		0: '',
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
	}[num%10]

def eat10s(num):
	def simple(num):
		return {
			0: '',
		#	1: ###complex###
			2: 'twenty',
			3: 'thirty',
			4: 'forty',
			5: 'fifty',
			6: 'sixty', 
			7: 'seventy',
			8: 'eighty',
			9: 'ninety',
		}[num/10%10] + ('-' if num%10!=0 and 
			num/10%10!=0 else '') + eat1s(num)
	def complex(num):
		return {
			10: 'ten',
			11: 'eleven',
			12: 'twelve',
			13: 'thirteen',
			14: 'fourteen',
			15: 'fifteen',
			16: 'sixteen',
			17: 'seventeen',
			18: 'eighteen',
			19: 'nineteen',
		}[num%100]
	if 10<=num<20: return complex(num)
	else: return simple(num)

def eat100s(num):
	if num < 100: return eat10s(num % 100)
	else: 
		rest = eat10s(num % 100)
		return eat1s((num % 1000) / 100) + ' hundred' + ((' and '+ rest) if rest else '')

def eat1000s(num):
	if num >= 1000:
		rest = eat100s(num%1000)
		return eat1s(num%10000/1000) + ' thousand' + ((' and '+rest) if rest else '')
	else: return eat100s(num)

def num2words(num):
	return eat1000s(num)

def count_nwsp_ndsh_letters(string):
	if string[0] in (' ','-'):
		return count_nwsp_ndsh_letters(string[1:])
	else: 
		if len(string) > 1:
			return 1 + count_nwsp_ndsh_letters(string[1:])
		else: return 1

words = [num2words(num) for num in xrange(1,1001)]
sum(map(count_nwsp_ndsh_letters,words))
