from lib import lcm

def smallest_modulo(lft, rgt):
    number = lcm(lft, lft + 1)
    for i in range(lft, rgt):
        number = lcm(i, number)
    return number

def solve():
    return smallest_modulo(1, 20)

def expected():
    return 232792560

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
