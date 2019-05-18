from datetime import date

def count_sundays(first_year, last_year):
    return sum(1
        for year in range(first_year, last_year + 1)
        for month in range(1, 13)
        if date(year, month, 1).weekday() == 6
    )

def solve():
    return count_sundays(1901, 2000)

def expected():
    return 171

def run():
    print("expected: {}\nresult:   {}".format(expected(), solve()))

if __name__ == "__main__":
    run()
