# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 23:20
# @Author  : stone
# @Email   : dangj@dqist.com
# @File    : guess.py
# @Software: PyCharm


_age_of_oldboy = 56

guess_age = int(input("guess age:"))

if guess_age == _age_of_oldboy :
    print("yes ,you got it ")
elif guess_age > _age_of_oldboy:
    print("think smaller")
elif guess_age < _age_of_oldboy:
    print("think big")
else:
    print("error")


#print("no,please agen")
#print("no,please agen")

