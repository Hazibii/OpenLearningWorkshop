#Conditionals for hacker pals

#If statement controls the logic flow 
#If a statement is true do some else you something else

letter = input("Enter a letter in the alphabet (UPPER CASE ONLY)")
if letter == "A":
    print("You entered A")
else:
    print("You entered a letter that wasn't A")

#We might however want to support nultiple possible choices. In this case upper and lower

letter = input("Enter a letter in the alphabet")
if letter == "a" or letter == "A":
    print("You entered a")
else:
    print("You entered a letter that wasn't a")

#The or keyword makes the condition if one of it's inputs is true
#The and keyword makes the condition true if both of it's inputs are true
#The not keyword makes the condition the inverse

#We might want to choose from multiple paths so we can use elif - which is the same as saying else then if
letter = input("Enter a letter in the alphabet")
if letter == "a" or letter == "A":
    print("You entered a")
elif letter == "b" or letter == "":
    print("You entered b")
else:
    print("You entered a letter that wasn't a")

#Sometimes we might want to assign a value depending on another value. We can do this in one line which is cleaner than a multi line if statement
letter = input("Enter a letter in the alphabet")
is_letter_a = "You entered a" if letter == "a" else "You entered not a"
print (is_letter_a)
