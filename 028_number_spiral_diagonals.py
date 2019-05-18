def sum_diagonals(size):
    half_size_limit = int(size / 2) + 1
    total = 1
    for i in range(1, half_size_limit):
        rgt_num = i << 1
        vertex = rgt_num * (rgt_num - 1) + 1
        total += vertex * 4 + (rgt_num * 6)
    return total

def solve():
    return sum_diagonals(1001)

def expected():
    return 669171001

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
