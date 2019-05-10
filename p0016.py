from functools import partial
from lib import compose

def sum_pow_digits(power):
    r = 2 ** power
    f = compose(sum, list, partial(map, int), list, str)
    return f(r)

def solve():
    return sum_pow_digits(1000)

def run():
    print(solve())

if __name__ == "__main__":
    run()
