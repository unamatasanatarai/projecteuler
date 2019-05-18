from lib import iprime

def get_prime_number_at(position):
    cnt = 1
    for prime in iprime():
        if cnt == position:
            return prime
        cnt += 1

def solve():
    return get_prime_number_at(10001)

def expected():
    return 104743

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
