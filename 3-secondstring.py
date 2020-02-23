# Program asks a user to input a string and outputs 
# every second letter in reverse order

s = input ("Enter a sentence: ")

# using slicing to reverse a string because it seemed most simple
# information on reversing a string found on:
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

print (s[::-2])

# using statement [-2] because we need
# to move every 2. place backwards
