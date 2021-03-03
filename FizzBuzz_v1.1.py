# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 02:40:40 2021

@author: Roger
"""
x = 1
while x < 101:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1
