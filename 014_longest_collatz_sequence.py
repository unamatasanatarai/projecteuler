def collatz(number):
    arr = [number]
    while number > 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (3 * number) + 1
        arr.append(number)
    return arr

def find_longest_collatz_under(limit):
    longest = 0
    number = 0
    for i in range(837799, limit):
        r = collatz(i)
        if len(r) > longest:
            longest = len(r)
            number = i
    return number

def solve():
    # assert [13, 40, 20, 10, 5, 16, 8, 4, 2, 1] == collatz(13), "Collatz broken!"
    # assert find_longest_collatz_under(20) == 18, "Finding collatz broken"
    return find_longest_collatz_under(1_000_000)

def expected():
    return 837799

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
