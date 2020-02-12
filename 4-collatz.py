# Program that asks the user to input any positive integer and
# outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and,
# if it is even, divide it by two,
# if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

x = int(input("Add any positive integer: "))

# used print () function "end" parameter to print all
# "x" values in one line
print (x, end = " ")

# while loop implemented to stop the program when value is one
while x > 1:

    # checking if number is even using modulus
    # to check if remainder after division is zero
    if x % 2 == 0:
        x = x / 2
        print (int(x), end = " ")
    
    # if the number has a remainder it performs other action
    else :
        x = (x*3) + 1
        print (int(x), end = " "),

# if user enters a negative integer program lets them know
# and asks for input again
if x < 1:
        print ("isn't a positive integer.")
        x = int(input ("Add any positive integer: "))

# I wanted to print all the answers in the same line 
# as in task example, and I  found a solution here:
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/