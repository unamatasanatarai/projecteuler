def sum_pseudo_narcissistic_numbers(length):
    hi = (9**length) * length
    total = 0
    cache = {}
    for n in range(0, 10):
        cache[str(n)] = n ** length
    # 1 is discarded
    for num in range(2, hi):
        if num == sum(cache.get(n) for n in str(num)):
            total += num
    return total


def solve():
    return sum_pseudo_narcissistic_numbers(5)


def run():
    print(solve())


if __name__ == "__main__":
    run()
