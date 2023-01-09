import math


def main(n):
    if (n == 0):
        return -0.09
    elif (n == 1):
        return -0.13
    elif (n >= 2):
        return (main(n - 2) ** 3 - main(n - 1) ** 2) ** 2 + main(n - 2)
