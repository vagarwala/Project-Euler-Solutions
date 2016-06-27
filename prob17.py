def NumInWords(n):
    import math
    numinwords = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
    }
    words = []
    ones = n % 10
    tens = n % 100
    hundreds = (n / 100) % 10
    thousands = n / 1000
    if n == 0:
        return "zero"
    if thousands:
        words.append(NumInWords(thousands))
        words.append('thousand')
        if not hundreds and tens:
            words.append('and')
    if hundreds:
        words.append(numinwords[hundreds])
        words.append('hundred')
        if tens:
            words.append('and')
    if tens:
        if tens < 10 or ones == 0:
            words.append(numinwords[tens])
        else:
            words.append(numinwords[tens - ones])
            words.append(numinwords[ones])
    return ' '.join(words)

def compute():
    total = 0
    for i in range(1, 1001):
        res = NumInWords(i)
        total += len(res.replace(' ', '').replace('-', ''))
    return total

print compute()