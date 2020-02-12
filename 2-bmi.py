# Week 2 assignment
# This program calculates your Body Mass Index (BMI) based on your height and weight

weight = float (input("Enter your weight in kg: "))
height = float (input("Enter your height in cm: "))

# BMI calculation is weight in centimeters devided by height in meters squared
# hm = height in meters

hm = height/100

BMI = weight / (hm**2)

# rounding of BMI to 2 points

BMIr = (round (BMI,2))

print ("Your BMI is", BMIr)
