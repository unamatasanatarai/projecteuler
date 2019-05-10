from lib import get_prime_factors

def smallest_multiple(lft, rght):
    print(set(get_prime_factors(24)).intersection(get_prime_factors(24)))
    print(set(get_prime_factors(24)))
    return 2520

def solve():
    return smallest_multiple(1, 20)

def run():
    print(solve())

if __name__ == "__main__":
    run()
