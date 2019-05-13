from lib import iprime

def get_prime_number_at(position):
    cnt = 1
    for prime in iprime():
        if cnt == position:
            return prime
        cnt += 1

def solve():
    return get_prime_number_at(10001)

def run():
    print(solve())

if __name__ == "__main__":
    run()
