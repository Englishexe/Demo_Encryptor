import os
import cryptocode
import maskpass
from time import sleep
password = maskpass.askpass(prompt="Password:", mask="*")
passwordtwo = maskpass.askpass(prompt="Confirm Password:", mask="*")
if passwordtwo == password:
    f = open("encrypted.info", "r")
    if f.read() == "0":
        f = open("key.key", "w")
        f.write(cryptocode.encrypt(password, password))
        f.close()
        os.system("cls")
        print("Changed your password")
    else:
        os.system("cls")
        print("You can not change the password while it is encrypted!")
else:
    os.system("cls")
    print("Password Doesn't match.")
    sleep(3)
    os.system("python encryptmypass.py")