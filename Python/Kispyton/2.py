def main(y):
    if (y < 102):
        return 9 * (31 * y - 34) ** 3
    elif (y >= 102) and (y < 131):
        return 47 * y - 83
    elif (y >= 131) and (y < 205):
        return 33 * (y + 16 + y ** 3 / 42) ** 3
    else:
        return y ** 12 - 80 - 69 * (y ** 3 + 86 * y) ** 2
