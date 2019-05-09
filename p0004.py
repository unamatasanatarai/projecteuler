def is_palindrome(string):
    string = str(string)
    if len(string) == 1:
        return True

    return string == string[::-1]

def find_all_palindromes(min, max):
    while min < max:
        if is_palindrome(min*max):
            print(min*max)
        min += 1

def solve():
    return find_all_palindromes(100, 999)

def run():
    print(solve())

if __name__ == "__main__":
    run()
