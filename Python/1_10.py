import random

def fast_mul(x, y):
    r = 0
    while y:
        if y & 1:
            r += x
        y >>= 1
        x += x
    return r

def fast_pow(x, y):
    r = 1
    while y:
        if y & 1:
            r *= x
        y >>= 1
        x *= x
    return r

def test():
    for i in range(1000):
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        assert fast_mul(x, y) == x * y
        assert fast_pow(x, y) == x ** y

test()
