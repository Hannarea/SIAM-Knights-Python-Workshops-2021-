# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:07:38 2021

@author: hreed
"""

import matplotlib.pyplot as plt
import numpy as np

#Problem 1 Solutions 

#Part [A]

def f(x):
    return 2*x**2+8*x-24

x = np.linspace(-10,10,100)

plt.plot(x,f(x),'b')
plt.title("Problem 1, Part A")
plt.show()


#Part [B]

def g(x):
    return 1/x

x = np.linspace(-1,1,100)

plt.plot(x,g(x),'r-')
plt.title("Problem 1, Part B")
plt.show()

#The problem is that python plots the points 
#and then draws straight lines from point to point
#the way to fix this is to plot the function piecewise
#The following plotting fixes the issue

x1 = np.linspace(-1,0,50)
x2 = np.linspace(0,1,50)

plt.plot(x1,g(x1),'r-')
plt.plot(x2,g(x2),'r-')
plt.title("Problem 1, Part B FIXED!")
plt.show()


#Part [C]

def gauss(x, mu, sig):
    coeff = 1/(sig*np.sqrt(2*np.pi))
    exponent = -1/2 * ((x-mu)/sig)**2
    return coeff * np.exp(exponent)


#Part [D]

x = np.linspace(-5,5,100)

plt.plot(x, gauss(x,0,1), 'r')
plt.plot(x, gauss(x,3,1), 'b')
plt.plot(x, gauss(x,0,0.5), 'g')
plt.title("Problem 1, Part D")
plt.show()


#Extra - How to make your graph fancy :) 
plt.plot(x, gauss(x,0,1), '--b' ,label = "graph 1")
plt.plot(x, gauss(x,1,1), ':r' , label = "graph 2")
plt.plot(x, gauss(x,0,2), '.g', label = "graph 3")
plt.plot(x, gauss(x, -3, 0.5), '-.y' ,label = "graph 4")
plt.title("Graph Title")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()



#Problem 2 Solutions 

#Part [A]

def special_sum(N):
    s = 0
    for i in range(N+1):
        s += (1/2)**(i-1)
        
    return s

print('Solution to problem 2, part A:\n')
print('N=10: ', special_sum(10))
print('N=100: ', special_sum(100))
print('N=1000: ', special_sum(1000))


#Part [B]

def fun(x):
    return x**2 * (x-2)

def riemann(N):
    x = np.linspace(1,2,N)
    delta_x = (2-1)/N
    s = 0
    for i in range(N):
        s += fun(x[i])*delta_x
    return s

print('Solution to problem 2, part B:\n')
print('N=10: ', riemann(10))
print('N=100: ', riemann(100))
print('N=1000: ', riemann(1000))


#Part [C]
def leftRiemann(f, a, b, N):
    x = np.linspace(a,b,N)
    delta_x = (b-a)/N
    s = 0
    for i in range(N):
        s += f(x[i])*delta_x
    return s

print("example using the functions from part B:\n")
print("leftRiemann(fun,1,2,10000) = ", leftRiemann(fun,1,2,10000))



        
        



             
      
      
      

