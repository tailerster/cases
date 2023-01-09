import math


def main(y):
    return math.sqrt(((math.tan(y)) ** 2 + 65 * y) / (52 + 45 * (63 * y ** 2 - 43 * y ** 3) ** 4)) \
           + (34 * (y ** 3 + y ** 2) - 74 * math.atan(y) ** 6) / y ** 5
