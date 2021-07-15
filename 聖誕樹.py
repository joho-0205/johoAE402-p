#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:34:47 2021

@author: joho
"""

num = int(input())
times = 2
for j in range(1,times+1):
    for i in range(1,num+1):
        print(" "*(num-i),"*"*i,end=(""))
        print("*"*(i-1))
print(" "*4,"|")
       
    