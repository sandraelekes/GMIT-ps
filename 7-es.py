# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line. 

import sys

# importing sys so it can take a command line argument
# sys.argv[1] beacuse sys.argv[0] is the first argument which is the name of py file we are starting
filename = sys.argv[1]

with open(filename, 'r') as f:
    es = f.read()
    # counting "e" character in the file
    count = es.count("e")
    # if we write count = es.count("e") + es.count("E") it will
    # give us a count of both upper and lowercase character
    print (count)


# sys.argv reference : https://www.geeksforgeeks.org/command-line-arguments-in-python/#sys
#                       https://docs.python.org/3.8/library/sys.html
# count reference: https://www.programiz.com/python-programming/methods/string/count