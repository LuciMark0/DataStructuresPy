# Fibonacci sequence using recursion
def get_fib(position):
    # Base cases
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        # Recursive call to get the Fibonacci value
        return get_fib(position - 2) + get_fib(position - 1)

# Test cases for Fibonacci sequence
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))

print("*" * 20)

# Quick sort using recursion
def quicksort(array):
    length = len(array)
    
    # Base case: if the array has 1 or fewer elements, it is already sorted
    if length <= 1:
        return array
    else:
        # Choose a pivot element (last element in this case)
        pivot = array.pop()

    # Create two empty lists for elements greater and lower than the pivot
    items_greater = []
    items_lower = []

    # Iterate through the remaining elements in the array
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    # Recursively sort the lower and greater elements, then concatenate the lists
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))

print("*" * 20)

# Bubble sort
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Test case for bubble sort
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble_sort(test))

print("*" * 20)

# Selection sort
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Test case for selection sort
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(selection_sort(test))

print("*" * 20)

# Insertion sort
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Test case for insertion sort
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(insertion_sort(test))