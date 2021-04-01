# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:13:40 2021

@author: hreed
"""

# # Problems for this week: 
#     1) Write a function which finds the nth Fibonaccin number. 
#        The function definition should be def fib(n)
#     2) Write a function to find the geometric mean of an array of data
#        The function definiton should be def g_mean(data)
#     3) Plot the sine function from 0 to 2pi. Use the online documentation of
#        matplotlib.pyplot.plot to label your axes, make a legend, and give 
#        your plot a title.   

import matplotlib.pyplot as plt
import numpy as np

### Problem 1

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    fib1 = 0
    fib2 = 1
    for i in range(n-2):
        #find the next number
        fib_next = fib1+fib2 
        
        #reset the two that you need to know for next time
        fib1 = fib2 
        fib2 = fib_next
    return fib2

#Example of using the function 
print(fib(13))




#### Problem 2

def g_mean(x):
    k = 1
    for i in range(len(x)):
        k *= x[i]
    return k**(1/len(x))

#example of using the function: 

data = np.array([1,2,3,4,2,3,4,1,2,1])
mean = g_mean(data)
print(mean)





### Problem 3

x = np.linspace(0,2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y)
plt.title('Sine Function')
plt.legend(['sin(x)'])
plt.xlabel('radians')
plt.ylabel('sin(x)')


