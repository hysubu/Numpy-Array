import numpy as np


# One dimensional array
num_ary = np.array([1 ,2,4])
print(num_ary)
print("type" , type(num_ary))


# Two Dimensional Array
two_dim_arry = np.array([[1, 3,2] , [2,4,5]])
print(two_dim_arry)
print("type" , type(two_dim_arry))


# Three Dimensional Array

three_dim_arry = np.array([[1,2], [2,3]  , [4,5]])
print(three_dim_arry)
print("type" , type(three_dim_arry))



# using Datatype create Array

use_flot = np.array([1 ,3,5], dtype=float)
print(use_flot)

use_str = np.array([1,2,4] , dtype=str)
print(use_str)

use_int = np.array([1,2,4] , dtype=int)
print(use_int)


use_bool = np.array([1,2,4] , dtype=bool)
print(use_bool)


use_complex = np.array([1,2,4] , dtype=complex)
print(use_complex)



# Using np.arange function

range_arry = np.arange(1,10,2) # start , end , step
print(range_arry)

range_arry_2 = np.arange(1,3)  # start , end
print(range_arry_2)




# Using np.Reshape()

reshape_ary = np.array([1,2,3,4,5,6]).reshape(3 , 2)  # 3 row , 2 ---column
print(reshape_ary)


# using np.ones() function

onse_ary = np.ones((3,4)) # bydefault its float datatype
# 3 ----number of rows
# 4 ----- number of columns
# onse_ary = np.ones((3 ,4),dtype=int)
print(onse_ary)
'''[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]'''

# using np.zeros() function
zero_ary = np.zeros((4 , 4))
print(zero_ary)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''


# using np.random()  function
# Its create random number between 0 to 1
rad_ary = np.random.random((4,3))
# 4 --- number of  row
# 3 --- number of columns
print(rad_ary)
'''
[[0.34034392 0.69401498 0.20889609]
 [0.98169904 0.50215897 0.57706511]
 [0.471474   0.99565361 0.59011863]
 [0.72341519 0.71206017 0.47473234]]
'''

# using np.linespace() function
ls_ary = np.linspace(9,10 ,10) # start , end , how many numbers elements generate between 9 to 10
print(ls_ary)
'''
[ 9.          9.11111111  9.22222222  9.33333333  9.44444444  9.55555556
  9.66666667  9.77777778  9.88888889 10.        ]
'''


# using ndim method
#  This method find the dimension of array like 1d or 2d or 3d

one_d = np.arange(10)
two_d = np.arange(8,dtype=float).reshape(2,4)
three_d = np.arange(8).reshape(2 ,2,2)
print(one_d.ndim) # 1
print(two_d.ndim) # 2
print(three_d.ndim) # 3

# Using shape method




