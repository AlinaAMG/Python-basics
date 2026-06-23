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

name = input("What is your name? : ")
age = int(input("How old are you? : "))

age = age + 1 

print(f"Hello {name}")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width 

print(f"The area is : {area} cm²")

# Exercise 2 Shopping Cart Program 

item = input("What item would you like to buy? : ")
price = float(input("What is the price : "))
quantity = int(input("How many would you like? : "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: {total} euros ")