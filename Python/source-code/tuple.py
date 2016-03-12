#!/usr/bin/python3
# Tuple.py 
# This is an exercise file from Open Learning Workshop
# Copyright 2016 Hacker Pals


#create a tuple
zoo = ('python', 'lion', 'penguin')

print ('Number of animals in the zoo is', len(zoo))

#new tuple
new_zoo = ('monkey', 'goat', zoo)

print ('Number of cages in the new zoo is', len(new_zoo))

print ('All animals in new zoo are', new_zoo)

print ('Animals brought from old zoo are', new_zoo[2])

print ('Last animal brought from old zoo is', new_zoo[2][2])

print ('Number of animals in the new zoo is', \len(new_zoo)-1+len(new_zoo[2]))
