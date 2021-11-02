# Creators: Samuel van Erk, Samuel Coady
# The program checks if a user is allowed to admit to a university or not, by asking several questions.
# Last edit: ...
# Python interpreter: Python 3.8.5
# Operating system: Microsoft Windows 10

import sys
import random

# Information block
print("\nInformation Block\n" +
"\nCreators: Samuel van Erk (s3283240), Samuel Coady (s3100405)" +
"\nYear of arrival in Leiden: 2021" +
"\nStudy Program: Sterrenkunde Bsc" + 
"\nName of the assignment: Admission Test" +
"\nTask user: the user will have to answer questions to determine if the user is allowed to apply for a course at the university." + 
"\nDate of creation: 31-10-2021\n")

# Function for asking the input of the user. If the type of the input is wrong, the program will end. 
def correct_input(date):
    try:
        date = int(input(f"Input the {date} you were born:\n"))
        return date
    except:
        print("Your input was wrong")
        sys.exit(1)
        

# Let user input date of birth using the function defined above.
birth_year = correct_input("year")
birth_month = correct_input("month")
birth_day = correct_input("day")

# Reference date
ref_year = 2021
ref_month = 10
ref_day = 19


# Check if the inputted value is correct, using several if-statements: e.g. month > 12 is incorrect.
wrong_output = False
if birth_day < 1 or birth_month < 1 or birth_month > 12 or birth_year > ref_year:   # checking for invalid input for months and years and if the birth_day is too low.
    wrong_output = True
if birth_month in (1, 3, 5, 7, 8, 10, 12) and (birth_day > 31):   # checking if the input for a 31-day month is too large   
    wrong_output = True
if birth_month in (4, 6, 9, 11) and (birth_day > 30):   # checking if the input for a 30-day month is too large
    wrong_output = True
if birth_month == 2:   # checking if the input for Februari is correct. 
    if birth_year % 4 == 0 and (birth_day > 29):
        wrong_output = True
    if birth_year % 4 != 0 and (birth_day > 28):
        wrong_output = True

if wrong_output: # If the output is incorrect, the user will exit the program.
    print("The output was wrong")
    sys.exit(1)


# Calculates the differences between reference date and inputted date 
year_difference = ref_year - birth_year 
month_difference = ref_month - birth_month
day_difference = ref_day - birth_day

# Calculates age
if day_difference < 0:   
    month_difference -= 1   
if month_difference < 0:    
    year_difference -= 1    
    month_difference += 12  

# Checks if its the users birthday on the reference date
isBirthday = False
if month_difference == 0 and day_difference == 0:   
    isBirthday = True

# Converts the age to months
age_in_months = 12*year_difference + month_difference   

# Prints the age
print(f"\nThe age of the user is {year_difference} years and {month_difference} months; {age_in_months} months.")
if isBirthday:
    print("Congratulations with your birthday!")
    

# Admission evaluation
if year_difference < 10 or year_difference > 100:
    print("Unfortunatey, you are too young or too old to apply. You've been rejected.")
    sys.exit(1)

# Day of the week 
day_of_the_week = input("\nInput the day of the week you were born (mo, tu, we, th, fr, sa, su): \n")

weekdays = ("su", "mo", "tu", "we", "th", "fr", "sa")

if day_of_the_week not in weekdays:
    print("Your input was wrong")
    sys.exit(1)

# For calculating the day of the week, we use an algorithm from https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
# For this calculation we need the century, the last two digids of the year and the month, starting in March (1 = March).

century = birth_year//100   # calculating the century, using floordivision

corrected_year = birth_year - century*100   # calculating the last two digids of the year
if birth_month < 3:   # Jan and Feb are treated as months of the previous year, so we subtract 1 from the year if the month is Jan or Feb.
    corrected_year -= 1

corrected_month = birth_month - 2   # we start counting the months from march, so we subtract 2 from the month.
if corrected_month < 1:   # if this gives a negative integer, 
    corrected_month += 12   # we convert it back to the corresponding month by adding 12.


# This is the formula for calculating the weekday corresponding to a date. It outputs a number 0-6 with 0 = sunday, 6 = saturday.
number_of_day_of_the_week = (birth_day + int(2.6*corrected_month - 0.2) - 2*century + corrected_year + int(corrected_year/4) + int(century/4))%7

actual_day_of_the_week = weekdays[number_of_day_of_the_week]   # converting the number to the corresponding weekday

if actual_day_of_the_week != day_of_the_week:
    print(f"Your answer was wrong. The correct answer was {actual_day_of_the_week}. You've been rejected")
    sys.exit(1)
else:
    print("Your answer was correct.")



## Exact Study
random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, int(10000/random_number1))
exactly_zero = random.randint(1, 10)   
if exactly_zero == 1:
    random_number2 = 0

try:
    product_guess = int(input(f"\nExact study test:\n\nPlease estimate the product of {random_number1} and {random_number2}: \n")) 
except:
    sys.exit(1)
    

actual_product = random_number1 * random_number2

lower_bound = int(actual_product - actual_product * 0.10)
upper_bound = int(actual_product + actual_product * 0.10)

if product_guess in range(lower_bound, upper_bound) or (random_number2 == 0 and product_guess == 0):
    print(f"Your answer of {product_guess} is correct. Anything between {lower_bound} and {upper_bound} would have been accepted")
    print(f"Congratulations, you have been accepted for an exact study")
    sys.exit(0)
else:
    print(f"Your answer of {product_guess} is incorrect. Anything between {lower_bound} and {upper_bound} would have been accepted")


## Social Study
if year_difference > 42:
    # https://en.wikipedia.org/wiki/The_Creation_of_Adam
    print("\nSocial study test: \n\nTry to answer this question correctly:" +
    "\nWhich of the following artist made the fresco \"The Creation of Adam\"?" +
    "\n\na. Vincent van Gogh\nb. Donatello\nc. Leonardo da Vinci\nd. Michelangelo Buonarroti")
    answer_question = input("\nPlease enter your answer (a, b, c, d):\n")
    
    if answer_question not in ("a", "b", "c", "d"):
        sys.exit(1)

    elif answer_question == "d":
        print("\nYour answer was correct. You've been admitted to social science!")
        sys.exit(0)
    else:
        print("\nYour answer was incorrect,. Unfortunately, you've been declined for social science...")
        sys.exit(1)
else:
    # https://en.wikipedia.org/wiki/Enigma_machine
    print("\nSocial study test: \n\nTry to answer this question correctly:" +
    "\nWhat is the name of the secret code, used by the Germans in the Second Worldwar?" +
    "\n\na. The Molotov-Ribbentropcode\nb. The Enigma\nc. The Vonn Schlieffencode\nd. The Morse code")
    answer_question = input("\nPlease enter your answer (a, b, c, d):\n")
    if answer_question not in ("a", "b", "c", "d"):
        sys.exit(1)

    elif answer_question == "b":
        print("\nYour answer was correct, you've been admitted to social science!")
        sys.exit(0)
    else:
        print("\nYour answer was incorrect,. Unfortunately, you've been declined for social science...")
        sys.exit(1)






