from lib import compose
from functools import partial

str_to_ints = compose(list, partial(map, int), list)
PIRAMID = list(map(lambda y: str_to_ints(y.split()), """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")))

def maximum_path(triangle):
    for y in reversed(range(len(triangle) - 1)):
        for x in range(len(triangle[y])):
            triangle[y][x] += max(triangle[y + 1][x], triangle[y + 1][x + 1])
    return triangle[0][0]

def test():
    assert maximum_path([
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]]) == 23

def solve():
    test()
    return maximum_path(PIRAMID)

def expected():
    return 1074

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
