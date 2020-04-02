# Problems 2020

<<<<<<< HEAD
This repository is used for the problem sets given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.\
Here I will explain how I came to the solution of given tasks, reference the sources I researched for solving the problems and list the technologies I used for creating and testing the code.\
I have previous knowledge and understanding of basics of coding in python so for some tasks I didn't require extensive research.


## Table of contents
* [Weekly tasks](#weekly-tasks)
    * [BMI](#bmi)
    * [Second string](#second-string)
    * [Collatz](#collatz)
    * [Weekday](#weekday)
    * [Square root](#square-root)
    * [Es](#es)
    * [Plotting](#plotting)
* [Technologies](#technologies)


## Weekly tasks

### ***BMI***

    Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared. 

This program is a basic calculation of a given formula based on the users input.\
User inputs the height in centimeters and weight in kilograms. The challenge here is not to forget to convert height from centimeters to meters in order to get the correct answer.\
Even though the formula could be done in one line, I chose to simplify the calculation by adding a new variable *hm*. This variable is used for converting height from centimeter to meters.\
I also added the [rounding](https://www.geeksforgeeks.org/round-function-python) of the result to 2 points for a nicer touch. The idea goes to another student.

User call of the program is :

```
λ python 2-bmi.py
```
User input :
```
Enter your weight in kg: 80
Enter your height in cm: 180
```
and the output is :

```
Your BMI is 24.69
```
  ### ***Second string***

    Write a program that takes asks a user to input a string and outputs every second letter in reverse order. 

There are couple of ways to solve this problem, but I chose the method of slicing because it's simple and only one line of code. The idea was found on [Geeksforgeeks.org](https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/).

The syntax of slicing is:
``` 
[start:stop:step]
```
*Start* and *stop* are default values as we need the whole sentence. *Step* is negative because we need the string in the reverse order. The value is 2 because we need every second letter from the reversed order.

User call of the program is :

```
λ python 3-secondstring.py
```
User input :
```
Enter a sentence: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
```
and the output is :

```
.uiaagmeoo eeoa utuiin omtdmueo e tl nciiarttenc,eatsrldmsimrL
```



  ### ***Collatz***
    
    Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

Even though the task didn't require to have a fix for wrongly inputed negative number, it's added to avoid errors. This is done with *while* loop.

In second *while* loop we are cheching whether a number is odd or even, with the help of conditional statements *if* and *else* and it's doing so until the current value is one.\
The statement *if* checks if the number is even using modulus operation. If the remainder of the operation is zero, the number is even and the program divides the number by 2 and prints it out.\
If the remainder is not zero, program performs operations from statement *else* - multiplying the number by three and adding one, and prints out the result.


User call of the program is :

```
λ python 4-collatz.py
```
User input :
```
Add any positive integer: -20
```
In case of putting in a negative integer the program will respond with a message that a number is negative and ask to input a positive integer until the input is correct:
```
Add any positive integer: -10
-10 isn't a positive integer.
Add any positive integer: -20
-20 isn't a positive integer.
Add any positive integer: 20
```

When user inputs the positive integer the output is :

```
20 10 5 16 8 4 2 1
```

  ### ***Weekday***

    Write a program that outputs whether or not today is a weekday.

  ### ***Square root***

    Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.\
    addition to the task: The weekly task is trickier than the previous ones but I really suggest you try to crack it.
    You'll find a simple algorithm for the problem if you Google "Newton's method for square roots".
    I really recommend trying to code it up yourself rather than looking at others' implementations.

  ### ***Es***

    Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line. 

  ### ***Plotting***
    
    Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. 
=======
This repository is used for the problem sets given during the Programming and scripting module.

## Weekly tasks

  ### *Week 1*


  ### *Week 2*


  ### *Week 3*


  ### *Week 4*


  ### *Week 5*


  ### *Week 6*


  ### *Week 7*


  ### *Week 8*


>>>>>>> a40f46715354556ec75ab55bee646af49af8bf6a

## Technologies

  * Visual Studio Code - version 1.43.2
  * Cmder - version 1.3.14.982



