def is_palindrome(string):
    string = str(string)
    if len(string) == 1:
        return True

    return string == string[::-1]

def find_all_palindromes(min, max):
    results = []
    for x in range(min, max):
        for y in range(min, max):
            num = x*y
            if is_palindrome(num):
                results.append(num)

    return results

def solve():
    return max(find_all_palindromes(100, 999))

def run():
    print(solve())

if __name__ == "__main__":
    run()
