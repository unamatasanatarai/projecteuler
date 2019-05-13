from lib import lcm

def smallest_modulo(lft, rgt):
    number = lcm(lft, lft + 1)
    for i in range(lft, rgt):
        number = lcm(i, number)
    return number

def solve():
    return smallest_modulo(1, 20)

def run():
    print(solve())

if __name__ == "__main__":
    run()
