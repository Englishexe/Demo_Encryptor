import os
import cryptocode
import maskpass
from time import sleep
f = open("encrypted.info", "r")
if f.read() == "1":
    print("Files already encrypted!")
    sleep(3)
    exit(0)
f.close()
f = open("key.key", "r")
password = maskpass.askpass(prompt="Password:", mask="*")
if not password == cryptocode.decrypt(f.read(), password):
    print("Incorrect password!")
    sleep(3)
    exit(0)
f.close()
os.chdir("Encrypted Contents")
files = []
for file in os.listdir():
    if file == "eApp.py" or file == "key.key" or file == "dApp.py":
        continue
    if os.path.isfile(file):
        files.append(file)
for file in files:
    f = open(file, "r")
    filecontents = f.read()
    f.close()
    f = open(file, "w")
    f.write(cryptocode.encrypt(filecontents, password))
    f.close()
os.chdir("..")
f = open("encrypted.info", "w")
f.write("1")
f.close()
print("Done")
sleep(3)