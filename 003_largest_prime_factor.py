def find_prime_factors(number):
    factors = []
    divisor = 2

    while(number > 2):
        if (number % divisor == 0):
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1

    return factors


def solve():
    return max(find_prime_factors(600851475143))

def run():
    print(solve())

if __name__ == "__main__":
    run()
