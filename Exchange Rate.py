#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:17:30 2021

@author: joho
"""

currency = input("Which currency do you want to exchange for Taiwan dollar?")
if currency == "YEN":
    currency_st = input("Do you want to use NTD or YEN as the benchmark?")
    if currency_st == "NTD":
        amount = int(input("Please enter the NTD amount"))
        amount_str = str(amount)
        yen = str(amount * 3.97)
        print(amount_str + "NTD can be converted into" + yen + "YEN")
    elif currency_st == "YEN":
        amount = int(input("Please enter the YEN amount"))
        amount_str = str(amount)
        ntd = str(amount * 0.25)
        print("Exchange" + amount_str + "YEN needs" + ntd + "NTD")
    else:
        print("ERROR "*100)
elif currency == "USD":
    currency_st = input("Do you want to use NTD or YEN as the benchmark?")
    if currency_st == "NTD":
        amount = int(input("Please enter the NTD amount"))
        amount_str = str(amount)
        usd = str(amount * 0.036)
        print(amount_str + "NTD can be converted into" + usd + "USD")
    elif currency_st == "USD":
        amount = int(input("Please enter the USD amount"))
        amount_str = str(amount)
        ntd = str(amount * 28.02)
        print("Exchange" + amount_str + "USD needs" + ntd + "NTD")
    else:
        print("ERROR "*100)
elif currency == "GBP":
    currency_st = input("Do you want to use NTD or GBP as the benchmark?")
    if currency_st == "NTD":
        amount = int(input("Please enter the NTD amount"))
        amount_str = str(amount)
        gbp = str(amount * 0.026)
        print(amount_str + "NTD can be converted into" + gbp + "GBP")
    elif currency_st == "GBP":
        amount = int(input("Please enter the GBP amount"))
        amount_str = str(amount)
        ntd = str(amount * 38.66)
        print("Exchange" + amount_str + "GBP needs" + ntd + "NTD")
    else:
        print("ERROR "*100)
elif currency == "HKD":
    currency_st = input("Do you want to use NTD or HKD as the benchmark?")
    if currency_st == "NTD":
        amount = int(input("Please enter the NTD amount"))
        amount_str = str(amount)
        hkd = str(amount * 0.28)
        print(amount_str + "NTD can be converted into" + hkd + "HKD")
    elif currency_st == "HKD":
        amount = int(input("Please enter the HKD amount"))
        amount_str = str(amount)
        ntd = str(amount * 3.61)
        print("Exchange" + amount_str + "HKD needs" + ntd + "NTD")
    else:
        print("ERROR "*100)
elif currency == "CNY":
    currency_st = input("Do you want to use NTD or CNY as the benchmark?")
    if currency_st == "NTD":
        amount = int(input("Please enter the NTD amount"))
        amount_str = str(amount)
        cny = str(amount * 0.23)
        print(amount_str + "NTD can be converted into" + cny + "CNY")
    elif currency_st == "CNY":
        amount = int(input("Please enter the CNY amount"))
        amount_str = str(amount)
        ntd = str(amount * 4.33)
        print("Exchange" + amount_str + "CNY needs" + ntd + "NTD")
    else:
        print("ERROR "*100)
else:
    print("ERROR "*100)