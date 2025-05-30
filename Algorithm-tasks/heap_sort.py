# -*- coding: utf-8 -*-
"""heap_sort.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hkGAftKk55Rp9jYXDXMn9VgCq1Hy1CGB
"""

import random
import time
import matplotlib.pyplot as plt

def heapify(arr, n, i):   #method to heapify the sub-arrays
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):  #method sorting the array using heapsort
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def measure_time(arr):    #method for measuring time taken for the process each time
    start_time = time.time()
    heapSort(arr)
    end_time = time.time()
    return end_time - start_time

datas = [1000, 2000, 3000, 4000, 5000]    #different data sizes for each iteration
times = []

for length in datas:
    arr = [random.randint(1, 100000) for _ in range(length)]    #generating n(data) random numbers between 1 - 10000
    time_taken = measure_time(arr)
    times.append(time_taken)

plt.plot(datas, times, marker='o')
plt.xlabel('Size of array')
plt.ylabel('Time taken')
plt.title('Heap Sort')
plt.show()

