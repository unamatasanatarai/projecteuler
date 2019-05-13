from math import factorial

def sum_factorions():
    cache = {}
    for x in range(0, 10):
        cache[str(x)] = factorial(x)
    limit = 7 * cache.get("9") + 1
    tot = 0
    for num in range(3, limit):
        s = sum(cache.get(i) for i in str(num))
        if s == num:
            tot += num
    return tot

def solve():
    return sum_factorions()

def run():
    print(solve())

if __name__ == "__main__":
    run()
