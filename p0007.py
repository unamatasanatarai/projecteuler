from lib import is_prime

def iprime():
    n = 2
    yield n
    while True:
        if is_prime(n):
            yield n
        n += 1

def get_prime_number_at(position):
    cnt = 0
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
