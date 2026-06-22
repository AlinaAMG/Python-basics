from math import *

print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

character_name= "Aryan"
character_age = 10

print(f"There was a little boy named '{character_name}', ")
print(f"He was {character_age} years old. ")
print(f"He really liked the name '{character_name}', ")
print(f"but didn't like beeing {character_age} years old. ")

my_num = -12
print(round(3.9))
print(floor(3.4))
print(ceil(3.5))
print(sqrt(36))

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age + " years old ")

# num1 = input("Enter a number: ")
# num2= input("Enter another number: ")
# # result = int(num1)+int(num2)
# result = float(num1) +float(num2)
# print(result)

# Mad Libs Game
# color = input("Enter a color: ")
# plural_noun = input("Answer a Plural Noun: ")
# celebrity = input("Enter a celebrity: ")


# print("Roses are " + color)
# print( plural_noun + " are blue")
# print("I love " + celebrity)

# Lists
lucky_numbers=[2, 7, 12, 3, 54, 105, 100]
friends = ["Mike", "Maria", "Mike", "John", "Anna", "Mira"]
friends[1]= "Julia"
print(friends[0])
print(friends[3])
print(friends[-1])
print(friends[1:])
print(friends[-2:4])

friends.sort()
print(friends)
lucky_numbers.sort()
# lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers)
friends.append("Kevin")
friends.insert(1, "Eline")
# friends.remove('Mira')
# friends.clear() # removes all the elements in de list
# friends.pop() # removes the last element in de list
print(friends.index("Kevin"))
print(friends.count("Mike"))
friends2 = friends.copy()
print(friends2)

# Tuples
coordinates = ((4, 5), (6,7), (80,45))
print(coordinates)
# coordinates[1] = 10 # krijg error
print(coordinates[0])

# Functions

def say_hi(name, age):
    print("Hello " + name + ". You are " + str(age) + " years old!" )

print("Top")
say_hi("Mike", 35)
say_hi("Alina", 43)
print("Bottom")

# Return statement

def cube(num):
    return num * num *num

result = cube(4)
print(result)


# if statements
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are a female or you are not tall")

# if Statements & Comparisons

def max_num(num1, num2, num3):
    if num1 >=num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2>=num3:
        return num2
    else: 
        return num3

print(max_num(12,80,5))

# Building a calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Invalid operator")


    # Dictionaries

monthConversions={
    "Jan": "January",
    "Feb": "February",
    "Mar":"Martch",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
# print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
# print(monthConversions["Luv", "Not a valid key"])

# While loop

i = 1
while i <=10:
    print(i)
    i += 1
print("Done with loop")

# Building a guessing game

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False


# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#          guess = input("Enter guess:  ")
#          guess_count+=1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
# else:
#     print("You win!")


# For loop
friends =["Alina", "Mike", "Aryan"]
print(len(friends))

for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")


# Exponent Function

print(2 ** 3) 

def raise_to_power(base_num, pow_num):
   result = 1
   for index in range(pow_num):
       result = result * base_num
   return result


print(raise_to_power(3,3))


# 2D Lists & Nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)

# Build a Translator
   
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():

               translation = translation + "G"
            else:
                translation= translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

# Try Except
try:
   answer=10/0
   number = int(input("Enter a number: "))
   print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")


# Reading Files
employees = {
    "Jim":"Salesman",
    "Paul":"Manager",
    "Maria":"Recruiter",
    "John" :"Accountant"
}

with open("employees.txt", "r+"):
    print(employees)

employee_file = open("employees.txt", "a")
employee_file.write("\nKelly - Customer Service")

# for employee in employee_file.readline():
#     print(employee)

print(employee_file.readable())
employee_file.close()

# Modules and pip
import useful_tools

print(useful_tools.roll_dice(10))


# CLASSES & OBJECTS
from Student import Student

student1 = Student("Jim", "Business", 3.6, False)
student2 = Student("Mike", "Recruiter", 4.2, True)


print(student1.name)
print(student2.major)
