#!/usr/bin/env python3
# -*- coding: utf-8 -*-```
"""
Created on Mon Aug  2 20:24:49 2021

@author: joho
"""

import random
word = {"有利的":"beneficial","狀態":"status","複習":"review","道歉":"apology","喜悅的":"pleased"}
while True:
    print("(1)Show All Vocabularies\n(2)Chinese to Eniglish Translate\n(3)English to Chinese Translate\n(4)Quiz\n(5)Save Dictionary\n(6)Exit")
    func = int(input())
    if func == 1:
        with open("字典.txt","r")as fo:
            show = fo.read()
        print(show)
    elif func == 2:
        print("Please enter the Chinese you want to translate")
        chi = input()
        checkchi = 0
        for i,j in word.items():
            if i == chi:
                checkchi = 1
                print("中文\t  英文")
                print(i,"\t",j)
                print()
        if checkchi == 1:
            continue
        else:
            print("ERROR")
    elif func == 3:
        print("Please enter the English you want to translate")
        eng = input()
        checkeng = 0
        for i,j in word.items():
            if j == eng:
                checkeng = 1
                print("英文\t  中文")
                print(j,"\t",i)
                print()
        if checkeng == 1:
            continue
        else:
            print("ERROR")
    elif func == 4:
        pts = 0
        for i in range(5):
            ques = random.choice(list(word))
            print(ques)
            ans = (input())
            yes = 0
            if word[ques] == ans:
                    yes  = 1
                    print("CORRECT")
                    pts = pts+20
            if yes == 0:
                print("WRONG")
        print("You got ",pts," points")
    elif func == 5:
        with open("字典.txt","w") as fo:
            count = 1
            for i,j in word.items():
                fo.write((str(count))+" : "+i+j+"\n")
                count = count+1
    elif func == 6:
        print("Thank You For Using Joho's Dictionary")
        break
    else:
        print("ERROR\n"*100)
        continue







