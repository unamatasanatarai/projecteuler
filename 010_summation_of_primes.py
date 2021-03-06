from lib import prime_sieve

def solve():
    return sum(prime_sieve(2_000_000))

def expected():
    return 142913828922

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
