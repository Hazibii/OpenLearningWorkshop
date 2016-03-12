#!/usr/bin/python3
# list.py 
# This is an exercise file from Open Learning Workshop
# Copyright 2016 Hacker Pals

ShoppingList = ['Mango', 'Banana', 'Juice', 'Cake', 'Soap']

#using len() to find the length of the list
print("I have", len(ShoppingList),'items to purchase')

#Using a for loop to print out all the items in the list
print("Theses items are, ")
for item in ShoppingList:
    print(item)

#The append function adds the next item(object) into the list
print("\nI also have to buy some rice.")
ShoppingList.append('rice')
print("My shopping list is now, ", ShoppingList)

#sort fucntion will sort the list alphabetically
print("I will sort my list now" )
ShoppingList.sort()
print("Sorted shopping list is ",ShoppingList)


print("The First item I will buy is", ShoppingList[0])
olditem = ShoppingList[0]
del ShoppingList[0]
#uisng del to delete the object on index '0'
print("I bought the", olditem)
print("My shopping list is now", ShoppingList)

