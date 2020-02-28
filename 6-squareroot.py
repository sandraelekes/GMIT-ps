# Write a program that takes a positive floating-point number as input
# and outputs an approximation of its square root. 
# Method used is called Newton's method

# Setting input to float type
x = float(input('Input positive floating-point number: '))

# Funny addition to check if the input number is a positive number
if x < 0:
    print ("Oops, your input is a negative number. I'm sure it's a mistake.")
    
    # Using abs() module to transform negative number into a positive number.
    x = abs(x)
    print ("I'll fix it for you:", x)

def sqrt(x):
        # varaible n is a guess that first iteration equals to the number we want to root
        n = x 
        
        # in while loop we are checking condition of convergence:
        # 1) values of x in two consecutive iterations are approximately equal; since
        # difference an be positive or negative, we use absolute value
        # 2) value of x*x - n becomes closer to zero
        while abs(x*x - n) > 0.001:
            # formula to calculate square root by Newton-Raphson method
            x = x - ((x*x - n)/(2*x))
        return x

# rounding floating result to 3 decimals
print ("The square root of ", x , "is approx. ", round(sqrt(x),3))

# reference:
# https://www.youtube.com/watch?v=szQUIRPrAgQ