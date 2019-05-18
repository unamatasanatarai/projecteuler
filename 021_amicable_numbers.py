from lib import proper_divisors

def amicable_numbers(limit):
    sumsums = {}
    for number in range(limit + 1):
        sumsums[number] = sum(proper_divisors(number))

    ret = []
    for pair in sumsums.items():
        num = pair[0]
        num_sum = pair[1]
        if num == num_sum:
            continue
        amicable = sumsums.get(num_sum)
        if amicable == num:
            ret.append(num)
            ret.append(num_sum)
    return set(ret)

def solve():
    return sum(amicable_numbers(10_000))

def expected():
    return 31626

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
