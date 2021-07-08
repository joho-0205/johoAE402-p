#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:18:58 2021

@author: joho
"""

man_age = int(input("How old are you?(man)"))
woman_age = int(input("How old are you?(woman)"))
if man_age>=18 and woman_age>=18:
    print("請男生先輸入自己的興趣")
    man_1 = input("What's your interest?")
    man_2 = input("What's your second interest?")
    man_3 = input("What's your third interest?")
    print("請女生輸入自己的興趣")
    woman_1 = input("What's your interest?")
    woman_2 = input("What's your second interest?")
    woman_3 = input("What's your third interest?")
    if man_1 == woman_1 or man_1 == woman_2 or man_1 == woman_3:
        if man_2 == woman_1 or man_2 == woman_2 or man_2 == woman_3:
            print("配對成功")
        else:
            if man_3 == woman_1 or man_3 == woman_2 or man_3 == woman_3:
                print("配對成功")
            else:
                print("配對失敗")
    else:
        if man_2 == woman_1 or man_2 == woman_2 or man_2 == woman_3:
            if man_3 == woman_1 or man_3 == woman_2 or man_3 == woman_3:
                print("配對成功")
            else:
                print("配對失敗")
        else:
            print("配對失敗")
else:
    print("You're not old enough.")
                
                
    
            
        
    
