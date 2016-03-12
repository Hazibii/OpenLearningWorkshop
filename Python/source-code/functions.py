#Functions 
#Functions allow us to reuse code

def maximum(a, b):
    """
    Return the greater of a and b
    """
    return a if a > b else b

number1 = int(input("First number "))
number2 = int(input("Second number "))
print("Maximum ", maximum(number1, number2)

#Remember the rule of three

#Recursion allows us to have a function call itself again

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#Try a few values
fib(1)
fib(4)
fib(20)

#How about
fib(20000)
fib(-1)

#What do you think will happen
