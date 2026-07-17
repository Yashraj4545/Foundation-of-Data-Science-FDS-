import numpy as np

#so there are two methods we can convert normal array to numpy array or create new numpy array

#first method 
arr1 = np.array([1,2,3])

#second method 
arr2 = [2,3,4]
arr2 = np.array(arr2)
#lets check 
print(arr2+arr1)

print(f"\n Array Dimensions \n")

#lets create 1D 2D 3D arrays
#1D
print("1D Array")
arr1d = np.array([1,2,3])
print(f"1D array Dimension: {arr1d.ndim}")
print(f"1D array Shape: {arr1d.shape}")
print(f"Printing its data type {arr1d.dtype}")
print(f"1D array strides new concept {arr1d.strides}") #New concept PENDING
print(arr1d)
print(f"its Address {arr1d.data}")

print(f"\n2D Array")
#2D array
#rows #column
arr2d = np.ones((2,2))
print(f"2D array Dimension: {arr2d.ndim}")
print(f"2D array Shape: {arr2d.shape}")
print(f"2D array strides: {arr2d.strides}")  #new
print(arr2d)

print(f"\n 3D array\n")

#lets create by ourself
arr3d = np.array([[[1,2,3],
                  [4,5,6]],
                  
                  [[7,8,9],
                   [10,11,12]]])     #_ row column
print(arr3d) 
#lets print perticular element 
print(f"\nprinting perticular element")
print(arr3d[1,0,2]) #it will print 9
print(f"3D array dimension: {arr3d.ndim}")
print(f"3D array shape: {arr3d.shape}")
print(f"3D array strides: {arr3d.strides}")

# we leaned 1D 2D and 3D array
