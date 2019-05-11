import importlib
import time
import sys

def to_ms(useconds):
    return round(useconds * 1000, 6)

def run_task(number, expected):
    module = importlib.import_module("p{}".format(number))
    return expected == module.solve()

def run():
    duration = 0
    passed = 0
    failed = 0

    for (task, expected) in TESTS.items():
        timeStart = time.time()
        result = run_task(task, expected)
        moduleDuration = time.time() - timeStart
        duration += moduleDuration
        msg = "\033[32m  ok  \033[0m"
        if result:
            passed += 1
        else:
            failed += 1
            msg = "\033[31m*FAIL*\033[0m"

        print("[ {} ] Task {}: {}ms".format(
            msg,
            task,
            to_ms(moduleDuration),
        ))

    print("\nall done^")
    print("duration:   {}ms".format(to_ms(duration)))
    print("failed:     {}".format(failed))
    print("passed:     {}".format(passed))


TESTS = {
    "0001": 233168,
    "0002": 4613732,
    "0003": 6857,
    "0004": 906609,
    "0006": 25164150,
    "0007": 104743,
    "0010": 142913828922,
    "0013": 5537376230,
    "0016": 1366,
    "0020": 648,
    "0028": 669171001,
    "0030": 443839,
    "0034": 40730,
}

if __name__ == "__main__":
    if len(sys.argv) == 2:
        timeStart = time.time()
        result = run_task(sys.argv[1], TESTS.get(sys.argv[1]))
        print("[ {} ] {}ms".format(result, to_ms(time.time() - timeStart)))
    else:
        run()
