from functools import lru_cache

# 1, 2, ... 19
ONE_NINETEEN = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# 10, 10, ... 90
TEN_NINETY = [3, 6, 6, 5, 5, 5, 7, 6, 6]
# 100, 1000, 1_000_000
SCALES = [7, 8, 7]

def number_to_counts(number):
    if number == 0:
        return [0]
    ret = []

    if number >= 100:
        zeros = len(str(number)) - 1
        index = zeros // 3
        hunds = number // (10**zeros)
        ret.append(ONE_NINETEEN[hunds - 1])
        ret.append(SCALES[index])
        number -= hunds * (10**zeros)
        if 100 > number > 0:
            ret.append(3)  # "and"

    if number >= 20:
        tens = number // 10
        ret.append(TEN_NINETY[tens - 1])
        number -= tens * 10

    if 0 < number < 20:
        ret.append(ONE_NINETEEN[number - 1])
        number -= number

    return ret

def count_letters(number):
    return sum(number_to_counts(number))

def test():
    assert count_letters(2222) == 33
    assert count_letters(2001) == 17
    assert count_letters(1001) == 17
    assert count_letters(1000) == 11
    assert count_letters(342) == 23
    assert count_letters(156) == 21
    assert count_letters(115) == 20
    assert count_letters(101) == 16
    assert count_letters(100) == 10
    assert count_letters(21) == 9
    assert count_letters(33) == 11
    assert count_letters(78) == 12
    assert count_letters(3) == 5
    assert count_letters(6) == 3
    assert count_letters(7) == 5
    assert count_letters(12) == 6
    assert count_letters(19) == 8
    assert count_letters(20) == 6
    assert count_letters(50) == 5
    assert count_letters(90) == 6
    assert count_letters_in_range(5) == 19

def count_letters_in_range(limit):
    return sum(count_letters(x) for x in range(limit + 1))

def solve():
    return count_letters_in_range(1000)

def expected():
    return 21124

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
