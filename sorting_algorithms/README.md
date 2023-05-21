## Fibonacci Sequence using Recursion

The `get_fib(position)` function calculates the Fibonacci value at a given position using recursion. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The function uses recursion to calculate the Fibonacci value by adding the values at `position - 2` and `position - 1`.

### Algorithm Explanation

1. If the given position is 0, the function returns 0.
2. If the given position is 1, the function returns 1.
3. For any other position, the function recursively calls itself with `position - 2` and `position - 1`.
4. The values returned by the recursive calls are added together to obtain the Fibonacci value at the given position.

### Example Usage

```python
print(get_fib(9))  # Output: 34
print(get_fib(11))  # Output: 89
print(get_fib(0))  # Output: 0
```

## Quick Sort
The `quicksort(array)` function implements the QuickSort algorithm to sort a given array in ascending order.

### Algorithm Explanation
- If the length of the array is 1 or less, it is already considered sorted and is returned.
- Choose a pivot element from the array (in this implementation, the last element).
- Partition the array into two subarrays: elements less than the pivot and elements greater than the pivot.
- Recursively apply QuickSort to the two subarrays.
- Concatenate the sorted subarrays and the pivot element to obtain the final sorted array.
 
### Example Usage
```python
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))  # Output: [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
```

## Bubble Sort
The `bubble_sort(array)` function implements the Bubble Sort algorithm to sort a given array in ascending order.

### Algorithm Explanation
- Iterate through the array from the first element to the second-to-last element.
- For each iteration, compare adjacent elements and swap them if they are in the wrong order.
- Repeat the above steps until the array is fully sorted.
 
### Example Usage
```python
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble_sort(test))  # Output: [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
```
## Selection Sort
The `selection_sort(array)` function implements the Selection Sort algorithm to sort a given array in ascending order.

### Algorithm Explanation
- Iterate through the array from the first element to the second-to-last element.
- For each iteration, find the minimum element in the remaining unsorted portion of the array.
- Swap the minimum element with the leftmost unsorted element.
- Repeat the above steps until the array is fully sorted.
 
### Example Usage
```python
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(selection_sort(test))  # Output: [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
```
