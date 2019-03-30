# ASSIGNMENT 1
Please write a simple CLI application in the language of your choice that does the following: Print the numbers from 1 to 10 in random order to the terminal. Please provide a README, that explains detailed how to run the program on MacOS and Linux.

(I don't have a MacOS Envrionment, so only linux version here)

# How to work on Linux:


## 1 Creat a python file (step1.png):
$ vi shufflenumber.py


## 2 write the code and save(step2.png)：

#!/usr/bin/python

#-*- coding: utf-8 -*-

import random

list = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(list)

print(list)


## 3 running the python file and see the result on the terminal(step3.png):
$ python3 shufflenumber.py

