#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:03:26 2021

@author: joho
"""

math = int(input("What's your math score?"))
english = int(input("What's your english score?"))
if math >= 90 and english>=90:
    print("你可以得到獎品")
elif (math<60 and english>=60 ) or (math>=60 and english<60):
    print("再加油")
elif math <60 and english<60:
    print("要處罰")
else:
    print("還ok啦")