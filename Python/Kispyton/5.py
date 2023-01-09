import math


def main(y):
    sum = 0
    n = len(y)
    for i in range(1, n + 1):
        sum += 91 * math.log10(y[n + 1 - math.ceil(i/4) - 1]) ** 4
    return sum
