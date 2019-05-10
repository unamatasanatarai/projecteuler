from lib import isEven


def ifibonacci(max):
    now = 1
    next = 1
    while True:
        if now > max:
            break
        yield now
        next, now = now + next, next

assert list(ifibonacci(10)) == [1, 1, 2, 3, 5, 8], "Fibonacci broken"

def solve():
    max = 4_000_000
    fib = sum(x for x in ifibonacci(max) if isEven(x))

    return fib

def run():
    print(solve())

if __name__ == "__main__":
    run()

