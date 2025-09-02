# Question 15:
# Using DateTime module to get current date and time
import datetime as dt 
now = dt.datetime.now()
print("Current date and time: ", now)

# Extracting full month name from current date
today = dt.date.today()
print(today.strftime("%B"))

# Question 16:
# Creating a 2 parameter function
def greet(first_name, day_name="Sunday"):
    greeting = f"Hi {first_name}! Happy {day_name}!"
    print(greeting)

# Calling the function with one and both parameters
greet("Anissea", "Sunday")
greet("Anissea")

# Question 17:
# Creating an Exception handling function using try, except, else, and finally
try: 
    numerator = 10 
    denominatoer = 0
    result = numerator / denominatoer
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("The result is:", result)
finally:
    print("Done.")
