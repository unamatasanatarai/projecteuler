import importlib
import time
import sys

def toMs(useconds):
    return round(useconds * 1000, 6)

def runTask(number, expected):
    module = importlib.import_module("p{}".format(number))
    return expected == module.solve()

def run():
    duration = 0
    passed = 0
    failed = 0

    for (task, expected) in TESTS.items():
        timeStart = time.time()
        result = runTask(task, expected)
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
            toMs(moduleDuration),
        ))

    print("\nall done^")
    print("duration:   {}ms".format(toMs(duration)))
    print("failed:     {}".format(failed))
    print("passed:     {}".format(passed))


TESTS = {
    "0001": 233168,
    "0002": 4613732,
    "0003": 6857,
    "0004": 906609,
}

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(runTask(sys.argv[1], TESTS.get(sys.argv[1])))
    else:
        run()
