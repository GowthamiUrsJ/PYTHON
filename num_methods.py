import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr_1d) 


arr_2d = np.array([[1, 2], [3, 4]])
print("2D Array:", arr_2d)


arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:", arr_3d)



zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
print("Zeros:", zeros)
print("Ones:", ones)


r = np.arange(1, 10) 
reshaped = r.reshape((3, 3))
print("Arange:", r) 
print("Reshaped to 3x3:", reshaped)

print("Array + 5:", arr_1d + 5)        
print("Array squared:", arr_1d ** 2)     
print("Sum:", np.sum(arr_1d))            
print("Max:", np.max(arr_1d))            
print("Mean:", np.mean(arr_1d))          


print("Flattened 2D array:", arr_2d.flatten()) 


print("\nTranspose of 2D array:\n", arr_2d.T)

