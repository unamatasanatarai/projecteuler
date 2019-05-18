from string import ascii_uppercase

DB = []
with open("022_input.txt", "r") as file:
    DB = list(map(lambda x: x.strip('"'), file.read().split(",")))
DB.sort()

LETTER_VALUES = {}
for letter in ascii_uppercase:
    LETTER_VALUES[letter] = ord(letter) - 64

def word_value(word):
    return sum(LETTER_VALUES[letter] for letter in word)

def sum_word_values():
    return sum(word_value(name) * (i + 1) for i, name in enumerate(DB))

def solve():
    return sum_word_values()

def expected():
    return 871198282

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
