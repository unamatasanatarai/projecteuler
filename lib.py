from functools import reduce
import math

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def isDivisible(n):
    def yesno(num):
        return num % n == 0
    return yesno

isEven = isDivisible(2)

def is_prime(number):
    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True

    if number %2 == 0:
        return False
    limit = int(math.sqrt(number))+1
    for test in range(3, limit):
        if number % test == 0:
            return False

    return True


def get_prime_factors(number):
    factors = []
    divisor = 2

    while(number > 2):
        if (number % divisor == 0):
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1

    return factors
