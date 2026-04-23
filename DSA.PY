import random
import time
import matplotlib.pyplot as plt

# Generate 10,000 random numbers
data = random.sample(range(1, 20000), 10000)

# Hash table
hash_table = {}
for num in data:
    hash_table[num] = True


# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Hash Search
def hash_search(table, target):
    return target in table


# Compare all
def compare(target):
    sorted_data = sorted(data)

    # Linear
    start = time.perf_counter()
    linear_search(data, target)
    linear_time = time.perf_counter() - start

    # Binary
    start = time.perf_counter()
    binary_search(sorted_data, target)
    binary_time = time.perf_counter() - start

    # Hash
    start = time.perf_counter()
    hash_search(hash_table, target)
    hash_time = time.perf_counter() - start

    print("\n===== RESULTS =====")
    print("{:<15} {:<15}".format("Algorithm", "Time Taken"))
    print("{:<15} {:<15f}".format("Linear", linear_time))
    print("{:<15} {:<15f}".format("Binary", binary_time))
    print("{:<15} {:<15f}".format("Hash", hash_time))

    # Graph
    names = ["Linear", "Binary", "Hash"]
    times = [linear_time, binary_time, hash_time]

    plt.bar(names, times)
    plt.title("Search Algorithm Speed Comparison")
    plt.ylabel("Time (seconds)")
    plt.show()


# Menu
while True:
    print("\n MENU ")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Hash Search")
    print("4. Compare All")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Goodbye")
        break

    target = int(input("Enter number to search: "))

    if choice == 1:
        start = time.perf_counter()
        result = linear_search(data, target)
        end = time.perf_counter()

        print("Result:", result)
        print("Time:", end - start)

    elif choice == 2:
        sorted_data = sorted(data)

        start = time.perf_counter()
        result = binary_search(sorted_data, target)
        end = time.perf_counter()

        print("Result:", result)
        print("Time:", end - start)

    elif choice == 3:
        start = time.perf_counter()
        result = hash_search(hash_table, target)
        end = time.perf_counter()

        print("Found:", result)
        print("Time:", end - start)

    elif choice == 4:
        compare(target)

    else:
        print("Invalid Choice")
