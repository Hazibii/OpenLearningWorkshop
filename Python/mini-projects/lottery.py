#!/usr/bin/python3
# Lottery.py 
# This is an exercise file from Open Learning Workshop
# Copyright 2016 Hacker Pals

import random

OzlotteryNumbers = []

#Main part of program
for i in range (0,7):
  number = random.randint(1,45)
  
  while number in OzlotteryNumbers:
    
    number = random.randint(1,45)
  
 
  OzlotteryNumbers.append(number)

#You Can comment the next line  
OzlotteryNumbers.sort()

print("Today's lottery numbers are: ") 
print(OzlotteryNumbers)
