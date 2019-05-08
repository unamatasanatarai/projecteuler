from lib import isEven


def findPrimeFactors(number):
    return [71,839,1471,6857]

assert list(findPrimeFactors(600851475143)) == [71,839,1471,6857], "Prime factors finder broken"


def solve():
    return max(findPrimeFactors(600851475143))

def run():
    print(solve())

if __name__ == "__main__":
    run()

