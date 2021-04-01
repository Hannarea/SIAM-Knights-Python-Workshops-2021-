# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:55:25 2021

@author: hreed
"""

# ###This is a intro to Python Tutorial###

# This is a comment, the computer will not read this as part of your code

#it is good practice to import any libraries you will use at the very top of your code! 
import numpy as np
import scipy.integrate as si
import numpy.linalg as la
import matplotlib.pyplot as plt

#variables and data

# #integers
# x=5
# print(x)
# print(type(x))

# #floats
# y = 4.354
# print('the value of y is ', y, ' and its type is ', type(y))

# #complex a + bj
# z=2+3j 
# print(z, type(z))

# #NOT complex
# j = 5
# k = 2+3*j
# print(k, type(k)) 

# #vector (np.array)
# v = np.array([1,2,3])
# print(v, type(v))

# #component wise operations
# print(5*v, 5+v)

# #Vector product i.e the dot product
# print(v@v)

# # #generating arrays of a certain size
# ones = np.ones(5)
# zeros = np.zeros(5)

# print(ones, zeros)

# #matrices (they are just arrays of arrays!!)
# matrix = np.array([ones, zeros, ones])
# print(matrix)
# #We can easily get the transpose using .T
# print(matrix.T)


# #matrix multiplication is similar to vector product
# print(matrix@matrix.T)

# #generating matrices is similar too!
# A = np.ones((5,5))
# print(A)
# B = np.eye(3)
# print(B)



### Loops ###
#Use loops when you want an action to be repeated a certain number of 
#times or until you get a desired result

# # ### When you know how many times you want something done, use a for loop
# x = 0
# for i in range(10): # from 0 to 4
#     x = x+i    
#     print("the value of x is  ", x)
#     print('hello')
# print("goodbye")   
    
# print('and now the for loop is done!')


# #Say you want to print some fibonacci numbers (recall: 0,1,1,2,3,5,8,13,...)
# n=20
# #initiate the first two 
# fib1 = 0
# fib2 = 1
# for i in range(n):
#     #find the next number
#     fib_next = fib1+fib2 
    
    # #reset the two that you need to know for next time
    # fib1 = fib2 
    # fib2 = fib_next
    
#     print('the ', i+3, 'th Fibbonacci number is ', fib_next)



### When you want something to happen until you get a result, use a while loop
# n,k = 0,100

# while (n!=k):
#     n+=1  # n = n + 1
#     k-=1  # k = k - 1
# print('n and k are equal at', n)  


# # what happens if the termination criterion is NEVER true??? Python, we have a problem... 
# print('waiting ... ')
# n,k = 1,100
# while (n!=k):
#     n+=1
#     k-=1
#     if (n>k):
#         print('Python, we have a problem ...')
#         break
# print('n and k are equal at', n, k) 


### Writing Funtions ###
# Functions are useful to break apart code into smaller chuncks that you 
# may reuse again and again. 

# def add(x,y):
#     ans = x+y
#     return ans # make sure you return something 
# x = np.array([1,2,3])
# print(add(x,2))


def function(x):
    return np.abs(4*(x-0.5)) # f(x) = |4(x-0.5)|

# #vectors can be passed into functions too! (anything, really - so long the operations are valid)
# #another vector generator!
x = np.linspace(0, 1, 100)
y = function(x)
print('the inputs were ', x, '\nand the ouputs were ',y)


plt.plot(x, y, 'bo')
plt.show()



# ### Some cool stuff from libraries!! ###

# #Integration from last week 
# ans, error = si.quad(function, 0, 1)
# print(ans, error) #Check it yourself!!

# #Solving matrix equations Ax = b
# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([1,1,1])
# x = la.solve(A,b)
# print(x)
# print('checking: A@x = ', A@x)

# #plotting data or functions 
# data = np.array([1,3,4,3,5,4,3,5,6,5,7,6,5,4,3,4,2,1,0,0])
# time = np.linspace(0,1,len(data))
# plt.plot(time, data, 'r*')
# plt.plot(time, function(time), 'b')


# # Problems for this week: 
#     1) Write a function which finds the nth Fibonaccin number. 
#         The function definition should be def fib(n)
#     2) Write a function to find the geometric mean of an array of data
#         The function definiton should be def g_mean(data)
#     3) Plot the sine function from 0 to 2pi. Use the online documentation of
#         matplkotlib.pyplot.plot to label your axes, make a legend, and give 
#         your plot a title.   


