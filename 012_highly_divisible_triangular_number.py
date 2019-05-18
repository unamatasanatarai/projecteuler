from lib import get_prime_factors
from collections import Counter
from itertools import count

def itriangle():
    triangle = 0
    for n in count(1, 1):
        triangle += n
        yield triangle

def find_number_for_divisibles(divisors_count):
    for triangle in itriangle():
        counts = Counter(get_prime_factors(triangle))
        tot = 1
        for i in counts.values():
            tot *= i + 1
        if tot > divisors_count:
            return triangle

def solve():
    return find_number_for_divisibles(500)

def expected():
    return 76576500

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
