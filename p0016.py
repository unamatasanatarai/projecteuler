from functools import partial, reduce
from lib import compose

def sum_pow_digits(power):
    r = 2 ** power
    f = compose(partial(map, int), list, str)
    return reduce(lambda c, t: c + t, f(r), 0)

def solve():
    return sum_pow_digits(1000)

def run():
    print(solve())

if __name__ == "__main__":
    run()
