#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:44:18 2021

@author: joho
"""
product = {"A001":{"小熊軟糖":20},"A002":{"冰棒":25},"A004":{"王子麵":10},"A006":{"汽水":30}}
while True:
    print("輸入貨號/退出/輸出所有產品")
    num = input()
    if num == "退出":
        break
    elif num == "輸出所有產品":
        print(" 貨號     品項   價格")
        for i,j in product.items():
            print(i,j)
    else:
        checkproduct = 0
        for i in product.keys():
            if i == num:
                checkproduct =1
        if checkproduct == 1:
            for i,j in product[num].items():
                print("product: ",i,"price: ",j)
        else:
            print("沒有這個號碼，要新加入請按1，重新輸入請按2")
            checknum = int(input())
            if checknum == 2:
                continue
            elif checknum ==1:
                newproduct = input("你的PRODUCT")
                newprice = input("PRICE")
                product[num]={newproduct:newprice}