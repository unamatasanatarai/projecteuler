from lib import is_divisible

is_divisible_by_3 = is_divisible(3)
is_divisibleBy5 = is_divisible(5)

def solve():
    return sum(x for x in range(1000) if is_divisible_by_3(x) or is_divisibleBy5(x))

def expected():
    return 233168

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()

