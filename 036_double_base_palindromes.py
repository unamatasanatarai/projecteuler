from lib import is_palindrome

def sum_double_base_palindromes():
    # even numbers end with 0, and those cannot be included
    return sum(x for x in range(1, 1_000_000, 2) if is_palindrome(x) and is_palindrome("{:b}".format(x)))

def solve():
    return sum_double_base_palindromes()

def expected():
    return 872187

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
