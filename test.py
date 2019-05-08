import importlib
import time

def toMs(useconds):
    return round(useconds*1000, 6)

def run():
    duration = 0
    passed = 0
    failed = 0

    for (task, expected) in TESTS.items():
        module = importlib.import_module("p{}".format(task))
        timeStart = time.time()
        result = module.solve()
        moduleDuration = time.time() - timeStart
        duration += moduleDuration
        msg = "\033[32m  ok  \033[0m"
        if result == expected:
            passed+=1
        else:
            failed+=1
            msg = "\033[31m*FAIL*\033[0m"

        print("Task {}, {}ms         [ {} ]".format(
            task,
            toMs(moduleDuration),
            msg
        ))

    print("\nFinished")
    print("duration:   {}ms".format(toMs(duration)))
    print("failed:     {}".format(failed))
    print("passed:     {}".format(passed))

TESTS = {
    "0001": 233168,
}

if __name__ == "__main__":
    run()
