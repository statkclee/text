# *- encoding: utf-8 -*-
import os

print(os.getcwd())

file_path = os.path.join(os.getcwd(), "data\Pride_and_Prejudice_1342.txt")

print(file_path)

file = open(file_path, 'r') 

file = open('data/Pride_and_Prejudice_1342.txt', 'r') 


if file.mode == "r":
    contents = file.read()
    print(contents)
