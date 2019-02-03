
import getpass
# 密文密码

_username = 'dangjian'
_password = '123456'
username = input("username:")
password = input("password:")

#print(username,password)

if _username == username and _password == password :
    print("welcome user {name} login ...".format(name=username))
else:
    print("error")

print("error2")




