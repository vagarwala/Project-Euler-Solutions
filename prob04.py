def is_pal(n):
	return str(n) == str(n)[::-1]


def main():
	biggest = 0
	for x in range(100, 1000):
		for y in range(100, 1000):
			if is_pal(x*y) and x*y > biggest:
				biggest = x*y
	return biggest

print main()