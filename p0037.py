from lib import iprime, is_prime

def is_truncatable_prime(prime):
    if prime <= 7:
        return True

    remainders = []

    # right truncatable prime
    num = prime
    while num:
        if not is_prime(num):
            return False
        num //= 10

    num = prime
    index = 1
    while num:
        remainders.append(num % 10 * index)
        num //= 10
        index *= 10

    # left truncatable prime
    num = prime
    while num:
        if not is_prime(num):
            return False
        num -= remainders.pop()

    return True

def sum_truncatable_primes():
    max = 11
    total = 0
    beginings = ["2", "3", "5", "7"]
    not_having = {2, 4, 5, 6, 8}
    # middle can only be = [1, 3, 7, 9]
    for prime in iprime():
        if prime < 11:
            continue

        if str(prime)[0] not in beginings:
            continue

        sp = list(str(prime))
        del sp[0]
        if not_having.intersection(sp):
            continue

        if is_truncatable_prime(prime):
            total += prime
            max -= 1
        if not max:
            break

    return total

def solve():
    return sum_truncatable_primes()

def run():
    print(solve())

if __name__ == "__main__":
    run()
