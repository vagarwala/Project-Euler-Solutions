def compute():
	longest_num = 1
	longest_length = 1
	for i in range(1, 1000000):
		chain = [i]
		while True:
			if chain[len(chain) - 1] != 1:
				if chain[len(chain) - 1] % 2 == 0:
					chain.append(chain[len(chain) - 1] / 2)
				else:
					chain.append(3*chain[len(chain) - 1] + 1)
			else:
				if len(chain) > longest_length:
					longest_length = len(chain)
					longest_num = i
				break
	return longest_num

print compute()