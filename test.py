import numpy as np

# 1-D Array example
a = np.array([23,4,2,12,2,23])
print("Print the one dimention array: a ")
print(a)
print("Print array dimentio (a.ndim): {}".format(a.ndim))
print("Get shape(a.shape)(Last one shows Item): {}".format(a.shape))
print("Get type (each value type) a: {}".format(a.dtype))
print("Item size (each item size) a: {}".format(a.itemsize))
print("Total elements in array (a.size): {}".format(a.size))
print("Totall memory size in bytes (a.nbytes): {}".format(a.nbytes))
print("Specific elemet select last element: {}".format(a[5]))

# 2-D Array example
b = np.array([[23,4,2,12,2,23],[45,33,23,3,23,4]], dtype='int8')
print("\nPrint the two dimention array: b ")
print(b)
print("Print array dimentio (b.ndim): {}".format(b.ndim))
print("Get shape(b.shape)(Last one shows Item): {}".format(b.shape))
print("Item size (each item type)(b.dtype) b: {}".format(b.dtype))
print("Item size (each item size byte)(b.itemsize) b: {}".format(b.itemsize))
print("Total elements in array (b.size): {}".format(b.size))
print("Totall memory size in bytes (a.nbytes): {}".format(a.nbytes))
print("Specific elemet select (leadst element): {}".format(b[1,5]))
print("Specific elemet select (leadst element): {}".format(b[1, -1]))
print("Select number of elements in array(b[0,:])): {}".format(b[0,:]))
print("Select number of elements in array (b[:,0])): {}".format(b[:,0]))
print("Select number of elements in array: {}".format(b[0,:4]))
print("Select number of elements in array: {}".format(b[1,:4]))
print("Select number of elements in array: {}".format(b[1,2:4]))
print("Select number of elements in array by gape 1(last): {}".format(b[1, 0::2]))
print("Select number of elements in array by gape 2(last): {}".format(b[1, 0::3]))
print("Select number of elements in array by gape by 1(last) start from 1 to 6: {}".format(b[1, 1:6:2]))
#Change element
b[1,5]=88
print("Change value of b array last element (b[1,5]=88)\n{}".format(b))
b[:,3]=[5,6]
print("Change value of b array multiple value at colum 4 (b[:,3]=[5,6])\n{}".format(b))

# 3-D Array eample:
c=np.array([[[1,3,4,6,3,3,23],[25,3,3,6,5,5,32],[9,7,5,3,1,4,6]]])
print("3D array: \n {}".format(c))
print("Shape of array: ",c.shape)
print("Dimention of Array: ",c.ndim)

d=np.array([[[1,2,8,12],[3,4,9,13],[16,17,18,19]],[[4,5,10,14],[6,7,11,15],[20,21,22,23]]])
print("3D array: \n {}".format(d))
print("Shape of Array: ",d.shape)
print("Dimention of Array: ",d.ndim)

print("Value at First in array: {}".format(d[0,0,0]))
# print("Value last {}".format()
