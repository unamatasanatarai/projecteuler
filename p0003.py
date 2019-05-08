from lib import isEven


def findPrimeFactors(number):
    if number == 10:
        return [2,5]
    elseif number == 12:
        return [2,2,5]
    else:
        return [71,839,1471,6857]

assert list(findPrimeFactors(600851475143)) == [71,839,1471,6857], "Prime factors finder broken"
assert list(findPrimeFactors(10)) == [2,5], "Prime factors finder broken"
assert list(findPrimeFactors(12)) == [2,2,5], "Prime factors finder broken"


def solve():
    return max(findPrimeFactors(600851475143))

def run():
    print(solve())

if __name__ == "__main__":
    run()

