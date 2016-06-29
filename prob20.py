import math
def compute():
	num = math.factorial(100)
	return sum([int(i) for i in str(num)])

print compute()