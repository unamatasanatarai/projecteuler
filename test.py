import importlib, time

def toMs(useconds):
    return round(useconds, 6)

def run():
    duration = 0

    for (task, expected) in TESTS.items():
        module = importlib.import_module("p{}".format(task))
        timeStart = time.time()
        result = module.calculate()
        moduleDuration = time.time() - timeStart
        duration += moduleDuration

        print("Task {}, {}s: {}".format(
            task,
            toMs(moduleDuration),
            "\033[32m pass \033[0m" if result == expected else "\033[31m*FAIL*\033[0m"
            ))

    print("Finished in {}s".format(toMs(duration)))


TESTS = {
    "0001": 233168,
}

if __name__ == "__main__":
    run()
