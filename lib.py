from functools import reduce
import math

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def isDivisible(n):
    def yesno(num):
        return num % n == 0
    return yesno

isEven = isDivisible(2)

def isPrime(number):
    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True

    if number %2 == 0:
        return False

    limit = int(math.sqrt(number))
    for test in range(3, limit, 2):
        if number % test == 0:
            return False

    return True


