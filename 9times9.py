#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:33:16 2021

@author: joho
"""

with open("9times9.txt","w") as fo:
    for i in range(1,10):
        for  j in range(1,10):
            fo.write(str(i)+"*"+str(j)+"="+str(i*j)+" ")
        fo.write("\n")