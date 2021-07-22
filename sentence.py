#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:15:36 2021

@author: joho
"""

import random
sentence = ["I","You","They","We","play","eat","drink","write","games","soda","pizza","homework"]
def choice():
    return random.sample(sentence,3)

sentence = choice()
print(sentence[0],sentence[1],sentence[2])