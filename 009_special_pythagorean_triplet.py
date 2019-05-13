def get_triplet_product(the_sum):
    for a in range(1, the_sum // 3):
        for b in range(a + 1, the_sum // 2):
            c = the_sum - a - b
            if a + b + c == the_sum and a**2 + b**2 == int(c ** 2):
                return a * b * c

def solve():
    return get_triplet_product(1000)

def run():
    print(solve())

if __name__ == "__main__":
    run()
