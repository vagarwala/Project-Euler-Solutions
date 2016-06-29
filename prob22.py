def main():
	f = open("names.txt", 'r')
	names = sorted([i.strip('"') for i in f.read().split(',')])
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	total = 0
	for i in range(len(names)):
		score = 0
		for char in names[i]:
			score += (alpha.index(char) + 1)
		total += score * (i + 1)
	return total

print main()