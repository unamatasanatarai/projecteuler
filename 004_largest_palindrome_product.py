from lib import is_palindrome

def find_all_palindromes(min, max):
    results = []
    for x in range(min, max):
        for y in range(min, max):
            num = x * y
            if is_palindrome(num):
                results.append(num)

    return results

def find_largest_palindrome_no_array(lft, rght):
    largest = 0

    for x in range(lft, rght):
        for y in range(lft, rght):
            num = x * y
            if num > largest and is_palindrome(num):
                largest = num

    return largest

def find_largest_palindrome(lft, rght):
    return find_largest_palindrome_no_array(lft, rght)

def solve():
    return find_largest_palindrome(100, 1000)

def expected():
    return 906609

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))
if __name__ == "__main__":
    run()
