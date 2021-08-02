#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:29:21 2021

@author: joho
"""

import random
import pickle
word = pickle.load(open("word_dic","rb"))
while True:
    print("(1)Show All Vocabularies\n(2)Chinese to Eniglish Translate\n(3)English to Chinese Translate\n(4)Quiz\n(5)Add Vocabs\n(6)Initialize\n(7)Exit")
    func = int(input())
    if func == 1:
        count = 0
        for i,j in word.items():
            count = count+1
            print(count,":",i,j)
            print()
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
        newchi = input("Please enter the Chinese you wanted to add.")
        neweng = input("Please enter the English you wanted to add.")
        word[newchi]=neweng
    elif func == 6:
        word = {"有利的":"beneficial","狀態":"status","複習":"review","道歉":"apology","喜悅的":"pleased"}
        print("Initialization Completed")
    elif func == 7:
        pickle.dump(word, open("word_dic","wb"))
        print("Thank You For Using Joho's Dictionary")
        break
    else:
        print("ERROR\n"*100)
        continue







