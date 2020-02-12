# Program asks a user to input a string and outputs 
# every second letter in reverse order

s = input ("Enter a sentence: ")

# using slicing to reverse a string without defining 
# the length of string because it is unknown

print (s[::-2])

# using statement [-2] because we need
# to move every 2. place backwards
