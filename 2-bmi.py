# Week 2 assignment
# This program calculates your Body Mass Index (BMI) based on your height and weight

weight = float (input("Enter your weight in kg: "))
height = float (input("Enter your height in cm: "))

# conversion of hight from cm to m using variable hm
hm = height/100

# BMI calculation is weight in kilograms devided by height in meters squared
BMI = weight / (hm**2)

print ("Your BMI is", round (BMI,2))

# credit for rounding BMI to 2 poins idea goes to to another student Jonathan Harper
# more information on rounding found on:
# https://www.geeksforgeeks.org/round-function-python
