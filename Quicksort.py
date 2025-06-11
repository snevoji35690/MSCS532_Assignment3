import random

def randomized_partition(arr, low, high):
    # Choose a random pivot index between low and high
    pivot_index = random.randint(low, high)
    # Swap the pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Example usage:
test_arrays = [
    [],                      # Empty array
    [3, 3, 3, 3],            # All duplicates
    [1],                    # Single element
    [5, 1, 4, 2, 8, 5, 3],   # General case
    [1, 2, 3, 4, 5]          # Already sorted
]

for i, test in enumerate(test_arrays):
    arr = test.copy()
    randomized_quicksort(arr)
    print(f"Test case {i + 1}: {arr}")

import random
import time
import sys

sys.setrecursionlimit(10000)  # increase for large arrays

# -------------------
# Sorting Algorithms
# -------------------

def randomized_quicksort(arr):
    def quicksort(low, high):
        if low < high:
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            pi = partition(low, high)
            quicksort(low, pi - 1)
            quicksort(pi + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(0, len(arr) - 1)

def deterministic_quicksort(arr):
    def quicksort(low, high):
        while low < high:
            pi = partition(low, high)
            # Recurse on the smaller partition to reduce recursion depth
            if pi - low < high - pi:
                quicksort(low, pi - 1)
                low = pi + 1
            else:
                quicksort(pi + 1, high)
                high = pi - 1

    def partition(low, high):
        pivot = arr[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[low], arr[i - 1] = arr[i - 1], arr[low]
        return i - 1

    quicksort(0, len(arr) - 1)


# -------------------
# Timing Function
# -------------------

def measure_time(sort_fn, data):
    arr = data.copy()
    start = time.time()
    sort_fn(arr)
    end = time.time()
    return (end - start) * 1000  # ms

# -------------------
# Test Config
# -------------------

def run_tests():
    sizes = [1000, 5000, 10000]
    test_cases = {
        "Random": lambda n: random.sample(range(n * 3), n),
        "Sorted": lambda n: list(range(n)),
        "Reversed": lambda n: list(range(n, 0, -1)),
        "Duplicates": lambda n: [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    }

    for size in sizes:
        print(f"\nArray size: {size}")
        for name, generator in test_cases.items():
            data = generator(size)
            t_rand = measure_time(randomized_quicksort, data)
            t_det = measure_time(deterministic_quicksort, data)
            print(f"{name:10}: Randomized = {t_rand:.2f} ms, Deterministic = {t_det:.2f} ms")

run_tests()

