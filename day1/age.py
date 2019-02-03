# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 23:30
# @Author  : stone
# @Email   : dangj@dqist.com
# @File    : age.py
# @Software: PyCharm


dj_age = 28

guess_age = int (input("aguess_age:"))

if guess_age == dj_age:
    print("yes ,you are good")
elif guess_age > dj_age:
    print("think smaller")
elif guess_age < dj_age:
    print("think big")

