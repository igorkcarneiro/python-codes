#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os

#finding files
files = []
for file in os.listdir():
    #ignore the .py file and the key file before using .append
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    # using .isfile to add files ONLY and nor directories
    if os.path.isfile(file):
        files.append(file)
print(files)

#this is the line of code that DIFFERS from the voldemort.py: it takes the key from thekey.key file and puts it into the secretkey variable
with open("thekey.key", "rb") as key:
    secretkey = key.read()

#asking the user to use the right input to decrypt the files:
secretphrase = "xablau"
user_phrase = input("Digite a chave para desencriptar: \n")

if user_phrase == secretphrase:
    for file in files:
        #rb is read bynary
        with open(file, "rb") as thefile:
            contents = thefile.read()
        #Here we are going to decrypt the files using the secretkey 
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        #after decrypting we have write it back to the contents_decrypted file
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("blz, desencriptei. Da mole nao bicho \n")
else:
    print("chave errada mano (。>︿<)\n")