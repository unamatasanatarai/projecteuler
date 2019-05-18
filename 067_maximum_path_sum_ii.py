PIRAMID = []
with open("067_input.txt", "r") as line:
    contents = line.read()
    PIRAMID = list(map(lambda row: list(map(int, row.split())), contents.split("\n")))
    # remove last item. Whilst read from file, additional "\n" is added
    del(PIRAMID[len(PIRAMID) - 1])

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
    return maximum_path(PIRAMID)

def expected():
    return 7273

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
