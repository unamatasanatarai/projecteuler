from lib import prime_sieve

def solve():
    return sum(prime_sieve(2_000_000))

def run():
    print(solve())

if __name__ == "__main__":
    run()
