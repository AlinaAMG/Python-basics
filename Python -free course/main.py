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

# is_student = False
# for_sale= True
# is_online= True

# print(f"Are you a tudent?: {is_student}")

# if is_student:
#     print("You are a student")
# else:
#     print("you are not a student")

# if for_sale:
#     print("That item is for sale")
# else:
#     print("That item is not AVAILABLE")

# if is_online:
#     print("You are online")
# else:
#     print("You are offline")

# Typecasting = the process of converting  a variable from one data type to another str(),  int(), float(), bool()

# name= "Alina Gabur"
# age = 42
# gpa = 3.2
# is_student = False

# type(name)
# print(type(name))

# gpa = int(gpa)
# print(gpa)

# age = float(age)
# print(age)

# age = str(age)
# print(type(age))

# name = bool(name)
# print(name)

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

# friends = 5
# friends += 1
# friends -= 2
# friends *= 3
# friends /= 2
# friends **= 2
# remainder = friends % 2


# print(friends)

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

# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))

# if unit == "C":
#     temp = round((9 * temp) /5+32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}°F")
# elif unit == "F":
#    temp = round((temp -32) *5 / 9, 1)
#    print(f"The temperature in Celsius is: {temp }°C")

# else:
#     print(f"{unit} is an invalid unit of measurement")



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

# credit_number = "1234-5678-9012-3456"

# credit_number = credit_number[::-1] # reverse string
# print(credit_number) 

# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])


# last_digits = credit_number[-4:]

# print(f"XXXX - XXXX - XXXX - {last_digits}")


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


# print(f"Price 1 is {price1:10}")
# print(f"Price 2 is {price2:10}")
# print(f"Price 3 is {price3:10}")

# WHILE LOOP = execute some code WHILE some condition remains true

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# while name == "":
#     print("You did  not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quite): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quite): ")
    
# print("bye")

# num = input("Enter a number between 1-10: ")

# while num < 1 or num > 10 :
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1-10: "))

# print(f"Your number is {num}")

# Python compound interest calculator

# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0 :
#         print("Principle can't be less than zero")
#     else:
#         break


# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0 :
#         print("Interest rate can't be less than zero")
#     else:
#         break

# while True:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than zero")
#     else:
#        break

# total = principle * pow((1 + rate / 100),time)
# print(f"Balance after {time}  year/s: ${total:.2f}")

# print(principle)
# print(rate)
# print(time)

# For loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

credit_card = "1234-5678-9012-3456"

# for x in (range(1, 11, 2)):
#     print(x) # 1,3,5,7,9

# print("HAPPY NEW YEAR")

# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x == 13:
#       break
#     else:
#         print(x)

# import time 
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# # time.sleep(3)

# print("TIME'S UP!")


#NESTED LOOP = A loop within another loop(outer,inner)
#             Outer Loop:
#                  inner loop:

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#       print(symbol, end ="")
#     print()

# collection = single "Variable" used to store multiple values
# List = [] ordered and changeable.Duplicated OK
# Set ={} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple =() ordered and unchangeable.Duplicates OK. Faster

fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
print("apple" in fruits) # True
print("pineapple" in fruits) # False

fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("orange")
fruits.insert(0, "pineapple")
# fruits.sort()
fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))
print(fruits.count("banana"))

print(fruits)
# for fruit in fruits:
#   print(fruit)


# SET

fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# print(fruits.add("Pineapple"))
fruits.remove("apple")
fruits.pop()
# fruits.clear()

print(fruits)

#Tuple

fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(fruits.index("apple"))
print(fruits.count("coconut"))

# Shopping cart program

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q": 
#         break
#     else: 
#         price = input(f"Enter the price of a {food}: $")
#         foods.append(food)
#         prices.append(price)

# print("-------YOUR CART-------")

# for food in foods:
#     print(food, end =" ")

# for price in prices :
#     total += price

# print(f"Your total is: ${total}")

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =["chicken","fish", "turkey"]

# groceries = [fruits, vegetables, meats]
# groceries = [['apple', 'orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]

# for collection in groceries:
#   for food in collection:
#     print(food, end=" ")
#   print()

# # print(groceries)

# num_pad = ((1, 2, 3),
#           (4,5,6), 
#           (7,8,9), 
#           ("*" , 0, "#"))

# for row in num_pad:
#     for num in row:
#         print(num, end = " ")
#     print()

# Python quiz game

# questions = ("How many elements are in de periodic table?: ",
#              "Which animal lays the largest eggs?: ",
#              "What is the most abundant gas in Earth's atmosphere?: ",
#              "How many bones are in the human body?: ",
#              "Which planet in the solar system is the hottest?: ")

# options = (("A. 116","B. 117", "C. 118", "D. 119"),
#            ("A. Whale","B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. Nitrogen","B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#            ("A. 206","B. 207", "C. 208", "D. 209"),
#            ("A. Mercury","B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("-----------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess = input("Enter(A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1

# print("------------------------")
# print("         RESULTS        ")
# print("------------------------")

# print("answers: ", end= "")
# for answer in answers:
#         print(answer, end = " ")
# print()

# print("guesses: ", end ="")
# for guess in guesses:
#         print(guess, end = " ")
# print()

# score = int(score / len(questions) * 100)
# print(f" Your score is: {score}%")

# DICTIONARY = a collection of {key:value} pairs ordered and changeable.No duplicates

# capitals  = {"USA": "Washington D.C",
#              "India":"New Delhi",
#              "China":"Beijing",
#              "Russia": "Moscow"
#             }

# # print(dir(capitals))
# # print(help(capitals))
# print(capitals.get("USA"))
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") # removes China
# capitals.popitem() # removes de last key-value that was inserted
# # capitals.clear() # clear the dictionary

# keys = capitals.keys()

# for key in  capitals.keys():
#     print(key)
# # print(keys)

# values = capitals.values()
# # print(values)
# for value in capitals.values():
#     print(value)
# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")
    

# print(capitals)

# Concession stand program
# menu = {
#     "pizza":3.00,
#      "nachos": 4.50,
#      "popcorn":6.00,
#      "fries":2.50,
#      "chips": 1.00,
#      "pretzel": 3.50,
#      "soda": 3.00,
#      "lemonade": 4.25,
#      "meat":10.99,
#      "vegetables":2.50
# }
# cart =[]
# total = 0
# print("-----------MENU----------")
# for key, value in menu.items():
#     print(f"{key}: {value:.2f}")
# print("-------------------------")

# while True:
#     food = input("Select an item (q to quite): ")
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print("-------YOUR ORDER---------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
# print(f"Total is: ${total:.2f}")

import random 

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q" , "K", "A"]


# number = random.randint(low, high)
# number = random.random() # random number between 0 and 1
# option = random.choice(options)
# print(option)
# print(number)
random.shuffle(cards)
print(cards)


# Python number guessing game

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:

#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high!Try again")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False

#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")


# print(answer)


# options = ("rock", "paper", "scissors")
# running= True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice(rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")
#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False

# print("Thanks for playing!")


# Dice roller program in python

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# # ● ┌ ─ ┐ │ └ ┘

# "┌──────────┐"
# "│          │"
# "│          │"
# "│          │"
# "└──────────┘"

# dice_art ={
#     1: ("┌──────────┐",
#         "│          │",
#         "│     ●    │",
#         "│          │",
#         "└──────────┘"),
#     2: ("┌──────────┐",
#         "│  ●       │",
#         "│          │",
#         "│       ●  │",
#         "└──────────┘"),
#     3: ("┌──────────┐",
#         "│  ●       │",
#         "│    ●     │",
#         "│       ●  │",
#         "└──────────┘"),
#     4: ("┌──────────┐",
#         "│  ●   ●   │",
#         "│          │",
#         "│  ●   ●   │",
#         "└──────────┘"),
#     5: ("┌──────────┐",
#         "│  ●   ●   │",
#         "│    ●     │",
#         "│  ●   ●   │",
#         "└──────────┘"),  
         
#     6: ("┌──────────┐",
#         "│  ●   ●   │",
#         "│  ●   ●   │",
#         "│  ●   ●   │",
#         "└──────────┘"),    
# }

# dice=[]
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))


# print(dice)

# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line],end="")
#     print()

# for die in dice:
#     total += die
# print(f"total: {total}")


# FUNCTION = a block of reusable code place () after the function name to invoke it


def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old {name}?")
    print(f"Happy birthday to {name}!")
    print()

print(happy_birthday("Aryan",10))
print(happy_birthday("Steve",40))

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount:.2f} is due on {due_date}")

display_invoice("Aryan", 42.50,"01/01")

# return = statement used to end a function and send a result back to the caller


def add(x,y):
    z= x+y
    return z 

def subtract(x,y):
    z= x-y
    return z

def multiply(x,y):
    z= x * y
    return z

def divide(x,y):
    z= x/y
    return z


print(add(4,9))
print(subtract(2,9))
print(multiply(10,12))
print(divide(12,89))

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last 


full_name = create_name("aryan", "orang")
print(full_name)

# default arguments  = A default value for certain parameters
#                      default is used when that argument is omitted
#                      make your functions more flexible, reduces number of arguments
#                     1. positional, 2. DEFAULT, 3.keyword, 4.arbitrary

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
print(net_price(500,0.1))


import time

def count(end,start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

print(count(0,10))

# args              = allows you to pass multiple non-key arguments
# ** kwargs         = allows you to pass multiple keywords-arguments
# keyword arguments = an argument preceded by an identifier
#                     allows you to pass multiple keyword-arguments
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. positional 2. default 3.KEYWORD 4.ARBITRARY

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# # hello("Hello", title = "Mr.", first = "Spongebob", last = "Squarepants")

# hello("Hello", title = "Mr.", last = "John", first ="James")

# for x in range(1, 11):
#     print(x,end=" ")

# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area,first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)

# Arbitrary arguments

# def add(a,b):
#     return a + b

# print(add(1, 2, 3))

# def add(*args): # je kan ook andere parameters gebruiken in plaats van args   
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3,4,5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.", 
              city="Detroit", 
              apt="100",
              state="MI", 
              zip="54321",)

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:    
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")}")
        print(f"{kwargs.get("pobox")}")
    else:
        print(f"{kwargs.get("street")}")

    print(f"{kwargs.get("city")} {kwargs.get("state")}, {kwargs.get("zip")}, {kwargs.get("pobox")}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street = "123 Fake St.",
               apt="#100",
               pobox ="PO box #1001",
               city= "Detroit",
               state="MI",
               zip= "54321")


# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]

# for number in  numbers:
#     print(number)

# for number in reversed(numbers):
#     print(number, end = " - ")

fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
#     print(fruit)

# name = "Bro Code"

# for character in name:
#     print(character, end = " ")

# Dictionary

my_dictionary = {"A": 1, "B": 2, "C": 3}

# for key in my_dictionary:
#     print(key)

# for value in my_dictionary.values():
#     print(value)

for key, value in  my_dictionary.items():
    print(f"{key}: {value}")


# Membership operators = used to test wether a value or variable is found in  a   #                        sequence(string, list, tuple, set or dictionary)
#                       1. in
#                       2. not in

# word = "APPLE"
# letter = input("Guess a letter in the secret word: ")

# if letter not in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# students = {"Spongebob", "Patrick", "Sandy"}
# student = input("Enter the name of a student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

# grades = {
#     "Sandy": "A",
#     "Squidward": "B",
#     "Spongebob":"C",
#     "Patrick":"D"
# }
# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# email = "BroCode@gmail.com"

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#    print("Invalid email")

#LIST COMPREHENSION =  A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [Expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x * 2)
    
# print(doubles)

doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]

print(doubles)
print(triples)
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars =[fruit[0] for fruit in fruits]

print(fruits)
print(fruit_chars)

# numbers = [1,-2, 3, -4, 5, -6, 8, -7]
# positive_nums = [num for num in numbers if num >= 0 ]
# negative_nums = [num for num in numbers if num < 0 ]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num  for num in numbers if num % 3 == 0]


# print(even_nums)
# print(positive_nums)
# print(negative_nums)

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]

# print(passing_grades)


# Match-case statement (switch): An alternative to using many "elif" statements
#                               Execute some code if a values matches a "case"
#                               Benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"

# print(day_of_week(4))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Monday"))

#module = a file containing code you want to include in your program
#         use "import" to include a module (built-in or your own)
#         useful to break up a large program reusable separate files

#import math
#import math as m 
#from math import pi
print(math.pi)

import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)
print(result)


# Variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

from math import e

print(e)

def func1():
    a = 1
    print(a)
    
def func2():
    b = 2
    print(b)

func1()
func2()


# if __name__ = __main__:(this script can be imported or run standalone )
#              Functions and classes in this module can be reused
#              without the main block of code executing
# ex.library = Import library for functionality
#            When running library directly, display a help page

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == "__main__":
    main()



# Python Banking Program

# def show_balance(balance):
#     print("********************")
#     print(f"Your balance is ${balance:.2f}")
#     print("********************")

# def deposit():
#     print("********************")
#     amount =float(input("Enter an amount to be deposited: "))

#     if amount <0:
#         print("********************")
#         print("That's not a valid amount")
#         print("********************")
#         return 0
#     else:
#         return amount

# def withdraw(balance):
#     print("***********************")
#     amount =float(input("Enter amount to be withdrawn: "))
#     print("***********************")

#     if amount > balance:
#         print("***********************")

#         print("Insufficient funds")
#         print("***********************")

#         return 0
#     elif  amount < 0:
#         print("***********************")

#         print("Amount must be greater than 0")
#         print("***********************")

#         return 0 
#     else:
#         return amount

# def main():
#     balance = 0
#     is_running = True

#     while is_running:
#         print("****************")
#         print("Banking Program")
#         print("****************")
#         print("1.Show Balance")
#         print("2.Deposit")
#         print("3.Withdraw")
#         print("4.Exit")
#         print("****************")

#         choice = input("Enter your choice (1-4): ")

#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#         elif choice == "3":
#            balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
#         else:
#             print("***************************")
#             print("That is not a valid choice")
#             print("***************************")

#     print("Thank you! Have a nice day!")

# if __name__ == "__main__":
#     main()
        

# Python Slot Machine

# def spin_row():
#     symbols = ["🍇", "🍉",  "🍋",  "🔔", "🌟"]

#     return [random.choice(symbols) for symbol in range(3)]

#     # results = []
#     # for symbol in range(3):
#     #     results.append(random.choice(symbols))
#     # return results

# def print_row(row):
#     print("***************")
#     print(" | ".join(row))
#     print("***************")
# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == "🍇":
#             return bet * 3
#         elif row[0] == "🍉":
#             return bet * 4
#         elif row[0] == "🍋":
#             return bet * 5
#         elif row[0] == "🔔":
#            return bet * 10
#         elif row[0] == "🌟":
#             return bet * 20
#     return 0 

# def main():
#     balance = 100
#     print("********************")
#     print("Welcome to Python Slots")
#     print("Symbols: 🍇 🍉 🍋 🔔 🌟")
#     print("********************")

#     while balance > 0 :
#         print(f"Current balance: ${balance}")

#         bet = input("Place your bet amount: ")

#         if not bet.isdigit():
#             print("Please enter a valid number")
#             continue

#         bet = int(bet)

#         if bet > balance:
#             print("Insufficient funds")
#             continue

#         if bet <= 0:
#             print("Bet must b e greater than 0")
#             continue

#         balance -= bet

#         row = spin_row()
#         print("Spinning...\n")
#         print(row)

#         payout = get_payout(row, bet)

#         if payout > 0:
#             print(f"You won ${payout}")
#         else:
#             print("Sorry you lost this round")

#         balance += payout

#         play_again = input("Do you want to spin again? (Y/N)")

#         if play_again !="Y":
#             break

#         print("**************************************")
#         print(f"Game over! Your final balance is ${balance}")
#         print("**************************************")


# if __name__ =="__main__":
#     main()


import string

chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")


print(chars)

# ENCRYPT

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")
