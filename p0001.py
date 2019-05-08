from lib import isDivisible

isDivisibleBy3 = isDivisible(3)
isDivisibleBy5 = isDivisible(5)

def solve():
    return sum(x for x in range(1000) if isDivisibleBy3(x) or
            isDivisibleBy5(x))

def run():
    print(solve())

if __name__ == "__main__":
    run()

