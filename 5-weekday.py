# A program that checks if today is weekday or weekend using a datetime module

# Importing the datetime module neccessary for this task
import datetime

# Returning the current local date and time with calssmethod datetime.now() via variable today
today = datetime.datetime.now()

# Returning the day of the week as integer with today.weekday() where Monday is 0, and Sunday is 6
# Bearing that integer in mind, I'm using if loop to check if todays day is a weekend or a weekday.
if today.weekday() > 4:
    print ("It is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")

# references:
# 1) video from the module learnonline: https://web.microsoftstream.com/video/77f26693-82ed-4006-8c22-c61d37e2f77f
# 2) https://docs.python.org/3/library/datetime.html#datetime.datetime.now