# -*- coding: utf-8 -*-
"""
@Author : SylarMei
"""

mun =  int(input("请输入一个自然数："))
count = 1
while mun != 1:
    if mun % 2 == 0:
        mun = mun//2
    else:
        mun = mun *3 + 1
    count += 1
print(count)

