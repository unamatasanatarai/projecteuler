from functools import reduce, partial
from lib import compose

def isDivisible(n):
    def yesno(num):
        return num % n == 0
    return yesno

isDivisibleBy3 = isDivisible(3)
isDivisibleBy5 = isDivisible(5)

def isDivisibleBy3Or5(n):
    return isDivisibleBy3(n) or isDivisibleBy5(n)

sumMultiplesOf3Or5 = compose(sum, partial(filter, isDivisibleBy3Or5))

def calculate():
    return sumMultiplesOf3Or5(range(1000))

def run():
    print(calculate())

if __name__ == "__main__":
    run()
