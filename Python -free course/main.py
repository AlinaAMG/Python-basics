print("i like vegetables")
print("It's really good")

# Types in python
# Strings
first_name = "Alina"
food="meat"
email="alina@yahoo.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 43
quantity = 3
num_of_students = 30
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float

price= 10.99
gpa = 3.2
distance = 5.5

print(f"the price is {price} euro")
print(f"Your gpa is {gpa}")
print(f"You run {distance} km")

# Boolean

is_student = False
for_sale= True
is_online= True

print(f"Are you a tudent?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("you are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not AVAILABLE")

if is_online:
    print("You are online")
else:
    print("You are offline")

# Typecasting = the process of converting  a variable from one data type to another str(),  int(), float(), bool()

name= "Alina Gabur"
age = 42
gpa = 3.2
is_student = False

type(name)
print(type(name))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(type(age))

name = bool(name)
print(name)

# input() = A function that prompts the user to enter data Returns the entered data as a string

# name = input("What is your name? : ")
# age = int(input("How old are you? : "))

# age = age + 1 

# print(f"Hello {name}")
# print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width 

# print(f"The area is : {area} cm²")

# Exercise 2 Shopping Cart Program 

# item = input("What item would you like to buy? : ")
# price = float(input("What is the price : "))
# quantity = int(input("How many would you like? : "))
# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: {total} euros ")

# Madlibs Game
# word game where you create a story
# by filling in blanks with random words

# adjective1 = input("Enter an adjective(description): ")
# noun1 = input("Enter a noun(person,place,thing ): ")
# adjective2 = input("Enter an adjective(description): ")
# verb1 = input("Enter a verb ending with ing: ")
# adjective3 = input("Enter an adjective(description): ")

# print(f"Today i went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}")

# OPERATORS

friends = 5
friends += 1
friends -= 2
friends *= 3
friends /= 2
friends **= 2
remainder = friends % 2


print(friends)

import math 

x = 9.6
y = 4
z= 5

# result = round(x)
# result = abs(y)
# result = pow(4,3)
# result = max(x,y,z)
# result = min(x,y,z)
# result = math.sqrt(x)
# result = math.ceil(x)
result = math.floor(x)

print(result)

print(math.pi)
print(math.e)



# Calculate circumference of a circle

# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference)}cm")

# # Calculate area of a circle
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi *pow(radius,2)

# print(f"The area of the circle is : {round(area,2)} cm²")


# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))

# c= math.sqrt(pow(a,2) + pow(b,2))

# print(f"Side C = {c}")


# If = Do some code only IF some condition is True
#  Else do something else

# age = int(input("Enter your age: "))

# if age >=100:
#     print("You are too old to sign up!")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You must be 18+ to sign up")

# response = input("Would you like food? (Y/N): ")

# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")

# name = input("Enter your name: ")

# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")

# for_sale = True

# if for_sale:
#     print("This item is for sale")
# else:
#     print("this item is NOT for sale")


 # Python calculator

# operator = input("Enter an operator ( + - * / ): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#    result = num1 + num2
#    print(round(result,3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result,3))
# elif operator =="*":
#     result = num1 * num2
#     print(round(result,3))
# elif operator == "/":
#    result = num1 / num2
#    print(round(result,3))
# else:
#     print(f"{operator} is not a valid operator")


# Python weight convertor

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is: {round(weight,1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# else:
#     print(f"{unit}  was not valid")

# Python temperature convertor

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) /5+32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
   temp = round((temp -32) *5 / 9, 1)
   print(f"The temperature in Celsius is: {temp }°C")

else:
    print(f"{unit} is an invalid unit of measurement")



# logical operators = evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be True
#                   and = both conditions must be True
#                   not = inverts the condition (not False, not True)

# temp = 36
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# temp = 28 
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("It is HOT outside ♨️")
#     print("It is SUNNY ☀️")
# elif temp <=0 and is_sunny:
#     print("It is COLD outside 🥶")
#     print("It is SUNNY 🌞")
# elif 28 > temp > 0 and is_sunny:
#     print("it is WARM outside 😁")
#     print("It is SUNNY ☀️")
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside ♨️")
#     print("It is CLOUDY ☁️")
# elif temp <= 0 and not is_sunny:
#     print("It is COLD outside")
#     print("It is CLOUDY ☁️")
# elif 28>temp > 0 and not is_sunny:
#     print("It is WARM outside")
#     print("It is CLOUDY ☁️")


# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#  Print or assign one of the values based on a condition
#  X if condition else Y


num = -3
a = 6
b = 7
age = 25
temperature = 10
user_role = "admin"


# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b

# print(max_num)
# print(min_num)

# status = "Adult" if age >= 18 else "Child"
# print(status)

# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full Access" if user_role== "admin" else "Limited Access"
# print(access_level)
# print(weather)


# String methodes
# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number")
# result = len(name)
# result = name.find(" ")
# name = name.capitalize()
# name = name.upper()
# name - name.lower()
# result = name.isdigit()
# result= name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", " ")
# print(result)
# print(help(str))


# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter a username: ")

# if len(username) >12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}")

# indexing = accessing elements of a sequence using [] (indexing operator) [start: end : step]

credit_number = "1234-5678-9012-3456"

credit_number = credit_number[::-1] # reverse string
print(credit_number) 

# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])


last_digits = credit_number[-4:]

print(f"XXXX - XXXX - XXXX - {last_digits}")


# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places(fixed point)
# :(number) = allocate that many spaces
#  :03 = allocate and zero pad  that many spaces
#  :< = left justify
#  :> = right justify
#  :^ = center align
#  :+ = use a plus sign to indicate positive value
#  := = place sign  to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# print(f"Price 1 is {price1:.2f}")
# print(f"Price 2 is {price2:.2f}")
# print(f"Price 3 is {price3:.2f}")


print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:10}")

# WHILE LOOP = execute some code WHILE some condition remains true

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# while name == "":
#     print("You did  not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

food = input("Enter a food you like (q to quite): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quite): ")
    
print("bye")

num = input("Enter a number between 1-10: ")

while num < 1 or num > 10 :
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))
    
print(f"Your number is {num}")
