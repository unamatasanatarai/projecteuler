def is_palindrome(string):
    string = str(string)
    if len(string) == 1:
        return True

    return string == string[::-1]

def solve():
    return is_palindrome("11")

def run():
    print(solve())

if __name__ == "__main__":
    run()
