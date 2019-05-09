from lib import is_prime
import math

def iprime():
    yield 2
    number = 3
    while True:
        if is_prime(number):
            yield number
        number += 2


def findPrimeFactors(number):
    factors = []
    divisor = 2

    while(number > 2):
        if (number % divisor == 0):
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1
    return factors


def solve():
    return max(findPrimeFactors(600851475143))

def run():
    print(solve())

if __name__ == "__main__":
    run()
