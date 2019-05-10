from lib import iprime

def sum_primes_below(limit):
    cnt = 0
    for prime in iprime():
        if (prime > limit):
            return cnt
        cnt += prime

def solve():
    return sum_primes_below(2_000_000)

def run():
    print(solve())

if __name__ == "__main__":
    run()
