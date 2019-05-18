def calculate_difference_for(numbers):
    sum_of_powers = sum([x * x for x in range(numbers + 1)])
    power_of_sum = ((numbers * (numbers + 1)) / 2) ** 2
    return power_of_sum - sum_of_powers

def solve():
    return calculate_difference_for(100)

def expected():
    return 25164150

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
