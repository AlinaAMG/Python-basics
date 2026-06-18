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




