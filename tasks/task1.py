import numpy as np

# Creating two arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Vertical stacking
vertical_stack = np.vstack((array1, array2))
print("Vertical Stack:\n", vertical_stack)

# Horizontal stacking
horizontal_stack = np.hstack((array1, array2))
print("Horizontal Stack:\n", horizontal_stack)


# Creating an array
arr = np.array([1, 2, 3, 4, 5])

# Searching for the index of a specific value
index_of_value = np.where(arr == 3)
print("Index of value 3:", index_of_value[0])

# Finding elements greater than 2
elements_greater_than_2 = np.where(arr > 2)
print("Elements greater than 2:", arr[elements_greater_than_2])


# Creating an array
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sorting the array
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

# Getting the indices that would sort the array
indices_for_sorting = np.argsort(arr)
print("Indices for Sorting:", indices_for_sorting)


# Creating an array
arr = np.array([1, 2, 3, 4, 5])

# Creating a filter for even numbers
even_filter = arr % 2 == 0

# Applying the filter
even_numbers = arr[even_filter]
print("Even Numbers:", even_numbers)


# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6])

# Splitting the array at index 3
split_arrays = np.split(arr, [3])
print("Split Arrays:", split_arrays)
