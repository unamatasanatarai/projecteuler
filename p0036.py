from lib import is_palindrome

def sum_double_base_palindromes():
    return sum(x for x in range(1_000_000) if is_palindrome(x) and is_palindrome("{:b}".format(x)))

def solve():
    return sum_double_base_palindromes()

def run():
    print(solve())

if __name__ == "__main__":
    run()
