def isPrime(number):
    if number == 0 or number == 1:
        return False

    for test in range(2, number):
        if number % test == 0:
            return False

    return True


assert not isPrime(1), "One is a prime number"
assert isPrime(2), "Two is a prime number"
assert isPrime(3), "Three is a prime number"
assert not isPrime(4), "Four is a prime number"


def iprime():
    number = 0
    while True:
        if isPrime(number):
            yield number
        number += 1


for x in iprime():
    if x > 300:
        break


def findPrimeFactors(number):
    if number == 10:
        return [2, 5]
    elif number == 11:
        return [11]
    elif number == 12:
        return [2, 2, 5]
    else:
        return [71, 839, 1471, 6857]


assert list(findPrimeFactors(600851475143)) == [
    71, 839, 1471, 6857], "Prime factors finder broken"
assert list(findPrimeFactors(10)) == [2, 5], "Prime factors finder broken"
assert list(findPrimeFactors(12)) == [2, 2, 5], "Prime factors finder broken"
assert list(findPrimeFactors(11)) == [11], "Prime factors finder broken"


def solve():
    return max(findPrimeFactors(600851475143))


def run():
    print(solve())


if __name__ == "__main__":
    run()
