from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def isDivisible(n):
    def yesno(num):
        return num % n == 0
    return yesno

isEven = isDivisible(2)

