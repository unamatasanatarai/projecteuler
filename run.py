import importlib
import time
import sys

def to_ms(useconds):
    return round(useconds * 1000, 6)

def run_task(task_file_name):
    mod_name = task_to_module(task_file_name)
    module = importlib.import_module(mod_name)
    expected = module.expected()
    ts = time.time()
    result = module.solve()
    te = time.time()
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


TASKS = [
    "001_multiples_of_3_and_5",
    "002_even_fibonacci_numbers",
    "003_largest_prime_factor",
    "004_largest_palindrome_product",
    "005_smallest_multiple",
    "006_sum_square_difference",
    "007_10001st_prime",
    "008_largest_product_in_a_series",
    "009_special_pythagorean_triplet",
    "010_summation_of_primes",
    "011_largest_product_in_a_grid",
    "012_highly_divisible_triangular_number",
    "013_large_sum",
    "014_longest_collatz_sequence",
    "015_lattice_paths",
    "016_power_digit_sum",
    "017_number_letter_counts",
    "020_factorial_digit_sum",
    "028_number_spiral_diagonals",
    "030_digit_fifth_powers",
    "034_digital_factorials",
    "036_double_base_palindromes",
    "037_truncatable_primes",
]
TESTS = {
    "001_multiples_of_3_and_5": 233168,
    "002_even_fibonacci_numbers": 4613732,
    "003_largest_prime_factor": 6857,
    "004_largest_palindrome_product": 906609,
    "005_smallest_multiple": 232792560,
    "006_sum_square_difference": 25164150,
    "007_10001st_prime": 104743,
    "008_largest_product_in_a_series": 23514624000,
    "009_special_pythagorean_triplet": 31875000,
    "010_summation_of_primes": 142913828922,
    "011_largest_product_in_a_grid": 70600674,
    "012_highly_divisible_triangular_number": 76576500,
    "013_large_sum": 5537376230,
    "014_longest_collatz_sequence": 837799,
    "015_lattice_paths": 137846528820,
    "016_power_digit_sum": 1366,
    "017_number_letter_counts": 1366,
    "020_factorial_digit_sum": 648,
    "028_number_spiral_diagonals": 669171001,
    "030_digit_fifth_powers": 443839,
    "034_digital_factorials": 40730,
    "036_double_base_palindromes": 872187,
    "037_truncatable_primes": 748317,
}

if __name__ == "__main__":
    if len(sys.argv) == 2:
        task = sys.argv[1]
        result = run_task(task)
        display_run(result.get("result"), task, result.get("duration"))
    else:
        run()
