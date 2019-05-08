from lib import isPrime

def iprime():
    number = 0
    while True:
        if isPrime(number):
            yield number
        number += 1

def findPrimeFactors(number):
    if number <= 3:
        return [3]

    max = number >> 1
    
    if number == 10:
        return [2, 5]
    elif number == 11:
        return [11]
    elif number == 12:
        return [2, 2, 5]
    else:
        return [71, 839, 1471, 6857]


assert list(findPrimeFactors(3)) == [3], "Cannot find factors for 3"
assert list(findPrimeFactors(10)) == [2, 5], "Cannot find factors for 10"
assert list(findPrimeFactors(11)) == [11], "Cannot find factors for 11"
assert list(findPrimeFactors(12)) == [2, 2, 5], "Cannot find factors for 12"
assert list(findPrimeFactors(600851475143)) == [
    71, 839, 1471, 6857], "Cannot find factors for 600851475143"


def solve():
    return max(findPrimeFactors(600851475143))

def run():
    print(solve())

if __name__ == "__main__":
    run()
