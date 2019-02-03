# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 0:16
# @Author  : stone
# @Email   : dangj@dqist.com
# @File    : me_while+if.py
# @Software: PyCharm


'''
1、只能猜3次
2、3次都错了提示
3、每一次错了要提示，
4、对了的话提示，并退出
'''
dj_age = 28
count = 0
while  count < 3 :
    guess_age = int(input("guess_age:"))

    if guess_age == dj_age:
        print("yes ,you got it")
        break

    elif guess_age > dj_age:
        print("think smaller")

    elif guess_age < dj_age:
        print("think big")

    count +=1

else:
    print("fuck off ")

