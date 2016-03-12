#!/usr/bin/python3
# loops.py 
# This is an exercise file from Open Learning Workshop
# Copyright 2016 Hacker Pals

#Most programs actually have a loop at their core
#While loops
#Repest the loop while the condition is true

while input("Enter a letter in the alphabet (q to quit)") != "q":
    print("Hello non q")
print("Finished")

#Break - exit out of a loop when a condition is met
while True:
    letter = input("Enter a letter in the alphabet (q to quit)")
    if letter == "q":
        break
    print("You entered ", letter)

#Continue - jump to the end of the loop and 
while True:
    letter = input("Enter a letter in the alphabet (q to quit, s to skip)")
    if letter == "q":
        break
    elif letter == "s":
        break
    print("You entered ", letter)

#for loop over a list of other collection and do some with each element in it

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

 
