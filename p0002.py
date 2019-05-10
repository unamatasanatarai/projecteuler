from lib import is_even, ifibonacci

def fibonacci_limited(max):
    for x in ifibonacci():
        if x > max:
            break
        yield x

def solve():
    max = 4_000_000
    fib = sum(x for x in fibonacci_limited(max) if is_even(x))

    return fib

def run():
    print(solve())

if __name__ == "__main__":
    run()

