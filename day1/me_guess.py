# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 11:50
# @Author  : stone
# @Email   : dangj@dqist.com
# @File    : me_guess.py
# @Software: PyCharm


dj_age = 28

count = 0

while count <3:

    guess_age = int(input("dj_age:"))

    if guess_age == dj_age:
        print("yes ,you are very good !!")
        break
    elif guess_age > dj_age:
        print("no ,think is smaller")
    else:
        print("no ,think is big")
    count +=1

    if count ==3:
        me_input  = input("DO you want to carry on ")

        if me_input != 'n':
            count =0
