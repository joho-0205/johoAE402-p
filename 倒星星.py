#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:35:04 2021

@author: joho
"""

num = int(input())
for i in range(num,0,-1):
    for j in range(i):
        print("*",end=(""))
    print()