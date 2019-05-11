def is_pseudo_narcissistic(number, power):
    powered = map(lambda n: int(n)**power, str(number))
    return sum(powered) == number


def sum_narcissistic_numbers(length):
    hi = (9**length) * length
    total = 0
    # 1 is discarded
    for num in range(2, hi):
        if is_pseudo_narcissistic(num, length):
            total += num
    return total


def solve():
    return sum_narcissistic_numbers(5)


def run():
    print(solve())


if __name__ == "__main__":
    run()
