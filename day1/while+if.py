# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 23:35
# @Author  : stone
# @Email   : dangj@dqist.com
# @File    : while+if.py
# @Software: PyCharm



'''
只能猜3次
对了提示
错了提示
'''
dj_age = 28

count = 0
while count <3:
    guess_age = int(input("dj_age:"))

    if guess_age == dj_age:
        print("yes ,you got it ")
        break
    elif guess_age > dj_age:
        print("think smaller")

    elif guess_age < dj_age:
        print("think big")
    count +=1
else:
    print("you have too time ,fuck off")



