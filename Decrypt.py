import os
import cryptocode
import maskpass
from time import sleep
f = open("encrypted.info", "r")
if f.read() == "0":
    print("Files not encrypted!")
    sleep(3)
    exit(0)
f.close()
f = open("key.key", "r")
password = maskpass.askpass(prompt="Password:", mask="*")
if not password == cryptocode.decrypt(f.read(), password):
    print("Incorrect password.")
    sleep(3)
    exit(0)
f.close()
os.chdir("Encrypted Contents")
files = []
for file in os.listdir():
    if file == "eApp.py" or file == "key.key" or file == "dApp.py" or file == "encrypted.info":
        continue
    if os.path.isfile(file):
        files.append(file)
for file in files:
    f = open(file, "r")
    filecontents = f.read()
    f.close()
    f = open(file, "w")
    filecontents = cryptocode.decrypt(str(filecontents), password)
    f.write(filecontents)
    f.close()
os.chdir("..")
f = open("encrypted.info", "w")
f.write("0")
f.close()
print("Done")
sleep(3)