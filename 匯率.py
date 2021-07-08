#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:56:45 2021

@author: joho
"""

# 日圓美金英鎊港幣人民幣
currency = input("你要將台幣換成哪一種貨幣？")
amount = int(input("請輸入台幣金額"))
amount_str = str(amount)
if currency == "日圓":
    yen = str(amount * 3.97)
    print("台幣" + amount_str + "元=" + yen + "日圓")
elif currency == "美金":
    usd = str(amount * 0.036)
    print("台幣" + amount_str + "元=" + usd + "美金")
elif currency == "英鎊":
    gbp = str(amount * 0.026)
    print("台幣" + amount_str + "元=" + gbp + "英鎊")
elif currency == "港幣":
    hkd = str(amount*0.028)
    print("台幣" + amount_str + "元=" + hkd + "港幣")
elif currency == "人民幣":
    cny = str(amount * 0.23)
    print("台幣" + amount_str + "元=" + cny + "人民幣")
    

    