import math


def main(m, p, a, b, x):
    sum0 = 0
    for c in range(1, m + 1):
        sum0 += p ** 2 - (c - 24 * p ** 3 - 95 * p ** 2) ** 5
    sum1 = 0
    for j in range(1, b + 1):
        sum2 = 0
        for c in range(1, a + 1):
            sum2 += (1 - j - 11 * x ** 2) ** 7 - j ** 9 - 74 * math.atan(c) \
                    ** 5
        sum1 += sum2
    return sum0 + sum1
