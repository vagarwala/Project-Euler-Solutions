def compute():
	squares = [i*i for i in range(1, 101)]
	nums = [i for i in range(1, 101)]
	return abs(sum(squares) - sum(nums)**2)

print compute()