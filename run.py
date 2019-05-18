from importlib import import_module
from glob import glob
from time import time
import sys

def to_ms(useconds):
    return round(useconds * 1000, 6)

def run_task(task_file_name):
    mod_name = task_to_module(task_file_name)
    module = import_module(mod_name)
    expected = module.expected()
    ts = time()
    result = module.solve()
    te = time()
    return {"result": result == expected, "duration": te - ts}

def task_to_module(task):
    return task.replace(".py", "")

def display_run(result, task, duration):
    msg = "\033[32m  ok  \033[0m" if result else "\033[31m*FAIL*\033[0m"
    print("[ {} ] Task {}:\t{}ms".format(
        msg,
        task[0:3],
        to_ms(duration),
    ))

def run():
    duration = 0
    passed = 0
    failed = 0

    for task in TASKS:
        result = run_task(task)
        duration += result.get("duration")
        if result.get("result"):
            passed += 1
        else:
            failed += 1

        display_run(result.get("result"), task, result.get("duration"))

    print("\nall done^")
    print("duration:   {}ms".format(to_ms(duration)))
    print("failed:     {}".format(failed))
    print("passed:     {}".format(passed))

TASKS = list(map(lambda file: file[2:][:-3], glob("./[0-9]*.py")))
TASKS.sort()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        task = sys.argv[1]
        result = run_task(task)
        display_run(result.get("result"), task, result.get("duration"))
    else:
        run()
