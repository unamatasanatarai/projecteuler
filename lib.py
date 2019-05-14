import math
from functools import reduce


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def is_divisible(n):
    def yesno(num):
        return num % n == 0
    return yesno


is_even = is_divisible(2)

# fastest yet
def is_prime(n):
    if n < 19:
        return n in [2, 3, 5, 7, 11, 13, 17]

    if not n % 2:
        return False
    if not n % 3:
        return False
    if not n % 5:
        return False
    if not n % 7:
        return False
    if not n % 11:
        return False
    if not n % 13:
        return False
    if not n % 17:
        return False
    if n < 361:
        return True

    if not n % 37:
        return False
    if not n % 97:
        return False
    if n < 31621:
        return pow(2, n - 1, n) == 1 and pow(3, n - 1, n) == 1

    for p in [19, 31, 41, 43, 73]:
        if not n % p:
            return False

    if n < 721801:
        return pow(2, n - 1, n) == 1 and pow(3, n - 1, n) == 1 and pow(5, n - 1, n) == 1

    if n < 1373653:
        temoins = {2, 3}
    elif n < 9080191:
        temoins = {31, 73}
    elif n < 4759123141:
        temoins = {2, 7, 61}
    elif n < 2152302898747:
        temoins = {2, 3, 5, 7, 11}
    elif n < 3474749660383:
        temoins = {2, 3, 5, 7, 11, 13}
    elif n < 341550071728321:
        temoins = {2, 3, 5, 7, 11, 13, 17}
    else:
        temoins = set(range(2, int(2 * math.log(n)**2)))

    s = 0
    d = n - 1
    while not d % 2:
        d >>= 1
        s += 1

    def test(a):
        "test de miller_rabin"
        x = pow(a, d, n)
        if x == 1:
            return False
        for r in range(s):
            if x == n - 1:
                return False
            x = x * x % n
        return True

    for p in temoins:
        if (not n % p):
            return False

    for p in temoins:
        if test(p):
            return False
    return True


# at least this one is mine.
def my_is_prime(number):
    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True

    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1
    for test in range(3, limit, 2):
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


def iprime():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def prime_sieve(limit):
    marks = [False, False] + [True] * (limit - 2)
    for (index, number) in enumerate(marks):
        if number:
            for n in range(index * 2, limit, index):
                marks[n] = False
    return [n for n in range(0, limit) if marks[n]]

def ifibonacci():
    now = 1
    next = 1
    while True:
        yield now
        next, now = now + next, next


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a

    while b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

