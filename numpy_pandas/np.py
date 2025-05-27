import numpy as np

# Create arrays using numpy

list = [1, 2, 3, 4, 5]
arr = np.array(list)

print("Array: ", arr)

# Attributes

print("Array shape: ", arr.shape)
print("Array size: ", arr.size)
print("Array dtype: ", arr.dtype)


# Basic indexing and slicing

print("Third element: ", arr[2])
print("First three elements: ", arr[:3])
print("Last two elements: ", arr[-2:])
print("Elements from index 1 to 3: ", arr[1:4])
print("Elements from index 1 to 4 with step 2: ", arr[1:5:2])
print("Elements greater than 2: ", arr[arr > 2])

# Create arrays with different methods

arr_zeros = np.zeros((3, 3))
print("3x3 array of zeros:\n", arr_zeros)
arr_ones = np.ones((2, 4))
print("2x4 array of ones:\n", arr_ones)
arr_identity = np.eye(3)
print("3x3 identity matrix:\n", arr_identity)

range = np.arange(0, 10, 2)
print("Array with range from 0 to 10 with step 2: ", range)

space = np.linspace(0, 1, 5)
print("Array with 5 evenly spaced numbers between 0 and 1: ", space)

# Dimensions (1D, 2D, 3D)

arr_1d = np.array([1, 2, 3])
print("1D array: ", arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr_2d)

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D array:\n", arr_3d)

# Mathematical operations and broadcasting

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Addition: ", arr1 + arr2)
print("Subtraction: ", arr1 - arr2)
print("Multiplication: ", arr1 * arr2)
print("Division: ", arr1 / arr2)
print("Exponentiation: ", arr1**2)

# Broadcasting example
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print("Broadcasting example: ", arr1 + arr3)

# Array manipulation

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr)
print("Flattened array: ", arr.flatten())
print("Reshaped array:\n", arr.reshape(3, 2))

# Statistics

arr = np.array([1, 2, 3, 4, 5])
print("Mean: ", np.mean(arr))
print("Median: ", np.median(arr))
print("Standard deviation: ", np.std(arr))
print("Variance: ", np.var(arr))

# Linear algebra
arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])

print("Dot product: ", np.dot(arr_a, arr_b))

