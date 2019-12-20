#creating a matrix a(3*3)
#arr=np.asarray(input("enter the matrix elements:")) with this user can enter elements
import numpy as np
arr=np.asarray([[-4.3,5,2],[1,7,-5],[0,-3,3]])
arr2=np.asarray([[3,4,2],[4,4,5],[2,5,6]])
print arr
print arr2
#functions of numpy in matrix
print"rounded values of matrix:\n",np.round(arr)
print"absolute values of matrix:\n",np.absolute(arr)
print"square of matrix:\n",np.square(arr)
print"maximum value of matrix:",np.max(arr)
print"minimum value of matrix:",np.min(arr)
print"transpose of matrix:\n",np.transpose(arr)
print"trace of matrix",np.trace(arr)
print"median of matrix",np.median(arr)
print"addition of two matrices:",np.add(arr,arr2)
print"subtraction of one matrix from another:",np.subtract(arr,arr2)
print"multiplication of two matrices:",np.multiply(arr,arr2)
print"inner product of two matrices:",np.inner(arr,arr2)
#functions of linear algebra in matrix
print"eigen values of matrix:\n",np.linalg.eig(arr)
print"inverse of a matrix:\n",np.linalg.inv(arr)
print"determinant value of given matrix :",np.linalg.det(arr)
print"rank:",np.linalg.matrix_rank(arr)
print"singular values of matrix:",np.linalg.svd(arr)
print"condition number of matrix:",np.linalg.cond(arr)
print"sign and natural logarithm for determinant value:",np.linalg.slogdet(arr)
n=input("enter number to be power of matrix:")
print"power of n to matrix\n",np.linalg.matrix_power(arr,n)


