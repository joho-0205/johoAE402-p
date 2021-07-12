#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:45:34 2021

@author: joho
"""

minnum = 1
maxnum = 100
com_min = 1
com_max = 100
import random
ques = random.randint(1,100)
innings = 1
pts = 0
com_pts = 0
while innings<=5 :
    print("請輸入", minnum ,"~" , maxnum)
    ans = int(input())
    com_ans = random.randint(com_min, com_max)
    print("電腦:", com_min ,"~" , com_max)
    print("電腦猜",com_ans)
    if ques>ans and com_ans != ques:
        minnum = ans
    elif ques<ans and com_ans != ques:
        maxnum = ans
    if ques<com_ans and ans != ques:
        com_max = com_ans
    elif ques>com_ans and ans != ques:
        com_min = com_ans
    if ques == ans and com_ans != ques:
        print("你得一分")
        pts = pts + 1
        com_pts = com_pts  
        innings = innings + 1
        ques = random.randint(1,100)
        minnum = 1
        maxnum = 100
        com_min = 1
        com_max = 100
    elif ques == ans and com_ans == ques:
        print("平手")
        pts = pts
        com_pts = com_pts
        innings = innings + 1
        ques = random.randint(1,100)
        minnum = 1
        maxnum = 100
        com_min = 1
        com_max = 100
    elif ques != ans and com_ans == ques:
        print("電腦得一分")
        pts = pts
        com_pts = com_pts + 1
        innings = innings + 1
        ques = random.randint(1,100)
        minnum = 1
        maxnum = 100
        com_min = 1
        com_max = 100
if pts > com_pts:
    print("YOU WIN")
elif pts < com_pts:
    print("YOU LOSE")
else:
    print("TIE")
        