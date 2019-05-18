from lib import binomial

def get_lattice_paths_count(side_length):
    path_length = side_length + side_length
    steps = side_length
    r = binomial(path_length, steps)
    return(r)

def solve():
    # assert get_lattice_paths_count(2) == 6, "Lattice paths broken"
    # assert get_lattice_paths_count(3) == 20, "Lattice paths broken"
    return get_lattice_paths_count(20)

def expected():
    return 137846528820

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
