from functools import partial, reduce
from lib import compose

def sum_factorial_digits(num):
    r = reduce(lambda c, t: c * t, range(1, num + 1), 1)
    f = compose(partial(map, int), list, str)
    return reduce(lambda c, t: c + t, f(r), 0)

def solve():
    return sum_factorial_digits(100)

def expected():
    return 648

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
