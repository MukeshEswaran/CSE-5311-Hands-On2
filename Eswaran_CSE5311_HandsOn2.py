import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def benchmark_sorting_algorithms(sizes):
    insertion_times = []
    selection_times = []
    bubble_times = []

    for size in sizes:
        data = random.sample(range(size * 10), size)

        # Insertion Sort
        start_time = time.time()
        insertion_sort(data.copy())
        insertion_times.append(time.time() - start_time)

        # Selection Sort
        start_time = time.time()
        selection_sort(data.copy())
        selection_times.append(time.time() - start_time)

        # Bubble Sort
        start_time = time.time()
        bubble_sort(data.copy())
        bubble_times.append(time.time() - start_time)

    return insertion_times, selection_times, bubble_times

input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
insertion_times, selection_times, bubble_times = benchmark_sorting_algorithms(input_sizes)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, insertion_times, label='Insertion Sort')
plt.plot(input_sizes, selection_times, label='Selection Sort')
plt.plot(input_sizes, bubble_times, label='Bubble Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Benchmark')
plt.legend()
plt.show()
