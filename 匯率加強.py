#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:57:11 2021

@author: joho
"""

currency = input("你要將台幣換成哪一種貨幣？")
if currency == "日圓":
    currency_st = input("請問您要以台幣還是日圓為基準?")
    if currency_st == "台幣":
        amount = int(input("請輸入台幣金額"))
        amount_str = str(amount)
        yen = str(amount * 3.97)
        print("台幣" + amount_str + "元可兌換成" + yen + "日圓")
    elif currency_st == "日圓":
        amount = int(input("請輸入日圓金額"))
        amount_str = str(amount)
        ntd = str(amount * 0.25)
        print("兌換" + amount_str + "日圓需要台幣" + ntd +  "元")
    else:
        print("ERROR "*100)
elif currency == "美金":
    currency_st = input("請問您要以台幣還是美金為基準?")
    if currency_st == "台幣":
        amount = int(input("請輸入台幣金額"))
        amount_str = str(amount)
        usd = str(amount * 0.036)
        print("台幣" + amount_str + "元可兌換成" + usd + "美金")
    elif currency_st == "美金":
        amount = int(input("請輸入美金金額"))
        amount_str = str(amount)
        ntd = str(amount * 28.02)
        print("兌換" + amount_str + "美金需要台幣" + ntd +  "元")
    else:
        print("ERROR "*100)
elif currency == "英鎊":
    currency_st = input("請問您要以台幣還是英鎊為基準?")
    if currency_st == "台幣":
        amount = int(input("請輸入台幣金額"))
        amount_str = str(amount)
        gbp = str(amount * 0.026)
        print("台幣" + amount_str + "元可兌換成" + gbp + "英鎊")
    elif currency_st == "英鎊":
        amount = int(input("請輸入英鎊金額"))
        amount_str = str(amount)
        ntd = str(amount * 38.66)
        print("兌換" + amount_str + "英鎊需要台幣" + ntd +  "元")
    else:
        print("ERROR "*100)
elif currency == "港幣":
    currency_st = input("請問您要以台幣還是港幣為基準?")
    if currency_st == "台幣":
        amount = int(input("請輸入台幣金額"))
        amount_str = str(amount)
        hkd = str(amount * 0.28)
        print("台幣" + amount_str + "元可兌換成" + hkd + "港幣")
    elif currency_st == "港幣":
        amount = int(input("請輸入港幣金額"))
        amount_str = str(amount)
        ntd = str(amount * 3.61)
        print("兌換" + amount_str + "港幣需要台幣" + ntd +  "元")
    else:
        print("ERROR "*100)
elif currency == "人民幣":
    currency_st = input("請問您要以台幣還是人民幣為基準?")
    if currency_st == "台幣":
        amount = int(input("請輸入台幣金額"))
        amount_str = str(amount)
        cny = str(amount * 0.23)
        print("台幣" + amount_str + "元可兌換成" + cny + "人民幣")
    elif currency_st == "人民幣":
        amount = int(input("請輸入人民幣金額"))
        amount_str = str(amount)
        ntd = str(amount * 4.33)
        print("兌換" + amount_str + "人民幣需要台幣" + ntd +  "元")
    else:
        print("ERROR "*100)
else:
    print("ERROR "*100)