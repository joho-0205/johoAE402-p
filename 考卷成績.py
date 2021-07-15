#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:35:04 2021

@author: joho
"""

st1=int(input("What score did student 1 get?"))
st2=int(input("What score did student 2 get?"))
st3=int(input("What score did student 3 get?"))
st4=int(input("What score did student 4 get?"))
st5=int(input("What score did student 5 get?"))
st6=int(input("What score did student 6 get?"))
st7=int(input("What score did student 7 get?"))
st8=int(input("What score did student 8 get?"))
st9=int(input("What score did student 9 get?"))
st10=int(input("What score did student 10 get?"))
scores=[st1,st2,st3,st4,st5,st6,st7,st8,st9,st10]
print("The average score is:",(scores[0]+scores[1]+scores[2]+scores[3]+scores[4]+scores[5]+scores[6]+scores[7]+scores[8]+scores[9])/10)
print("The highest score is",max(scores))
print("The lowest score is:",min(scores))