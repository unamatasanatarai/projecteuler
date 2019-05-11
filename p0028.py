def sum_diagonals(size):
    half_size_limit = int(size / 2) + 1
    total = 0
    for i in range(0, half_size_limit):
        rgt_num = i * 2
        lft_num = rgt_num - 1
        vertex = rgt_num * lft_num + 1
        if i == 0:
            vertices = 1
        else:
            vertices = vertex * 4 + (rgt_num * 6)
        total += vertices
    return total

def solve():
    return sum_diagonals(1001)

def run():
    print(solve())

if __name__ == "__main__":
    run()
