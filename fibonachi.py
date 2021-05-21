# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:17:54 2021

@author: User
"""

def fibonachi(n):
    fib_ketligi=[]
    for x in range(n):
       if x==0 or x==1:
           fib_ketligi.append(1)
       else:
           fib_ketligi.append(fib_ketligi[x-1]+fib_ketligi[x-2])
    return fib_ketligi
print(fibonachi(10)) 