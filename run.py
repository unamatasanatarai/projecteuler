from importlib import import_module
from glob import glob
from time import time
import sys

def us_to_time(seconds):
    mseconds = int((seconds - int(seconds)) * 1_000_000)
    seconds = int(seconds)
    minutes = int(seconds / (1000 * 60))
    return f"{minutes}m {seconds:02}s {mseconds:06}μs"


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
    print(f"[ {msg} ] Task {task[0:3]}:\t{us_to_time(duration)}")

def run():
    start = time()
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

    print(f"""
    run complete!
    run time:     {us_to_time(time() - start)}
    tasks time:   {us_to_time(duration)}
    failed:       {failed}
    passed:       {passed}
    """)

TASKS = list(map(lambda file: file[2:][:-3], glob("./[0-9]*.py")))
TASKS.sort()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        task = sys.argv[1]
        result = run_task(task)
        display_run(result.get("result"), task, result.get("duration"))
    else:
        run()
