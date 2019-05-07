from functools import reduce, partial

def isDivisible(n):
    def yesno(num):
        return num % n == 0
    return yesno

isDivisibleBy3 = isDivisible(3)
isDivisibleBy5 = isDivisible(5)

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def isDivisibleBy3Or5(n):
    return isDivisibleBy3(n) or isDivisibleBy5(n)

sumMultiplesOf3Or5 = compose(sum, partial(filter, isDivisibleBy3Or5))

print (sumMultiplesOf3Or5(range(2, 1000)))
