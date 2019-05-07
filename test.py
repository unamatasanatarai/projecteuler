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

        print("Task {}: {} [{}s]".format(
            task,
            " pass " if result == expected else "*FAIL*",
            toMs(moduleDuration)
            ))

    print("Finished in {}s".format(toMs(duration)))


TESTS = {
    "0001": 233168,
}

if __name__ == "__main__":
    run()
