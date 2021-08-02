#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:08:19 2021

@author: joho
"""

eng = input("Please enter english letters and numbers")
maxeng=""
mineng=""
if eng.isalnum():
    for i in range(len(eng)):
        if eng[i].isalpha():
                    if ord(eng[i])>=65 and ord(eng[i])<=90:
                         mineng = mineng+chr(ord(eng[i])+32)
                    else:
                        mineng = mineng+eng[i]
                    if ord(eng[i])>=97 and ord(eng[i])<=122:
                        maxeng = maxeng+chr(ord(eng[i])-32)
                    else:
                        maxeng = maxeng+eng[i]
        elif eng[i].isdigit():
            mineng = mineng+eng[i]
            maxeng = maxeng+eng[i]
else:
    print("ERROR"*100)
print("Upper Case + Numbers:",maxeng)
print("Lower Case + Numbers:",mineng)
            


