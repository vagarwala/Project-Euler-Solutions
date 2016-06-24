def compute():
	for a in range(1, 1000 + 1):
		for b in range(a + 1, 1000 + 1):
			c = 1000 - a - b
			if a * a + b * b == c * c:
				return a * b * c

print compute()