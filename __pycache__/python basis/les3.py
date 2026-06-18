# 1.
eten=["carpaccio"," steak","salade", "pannenkoek"]
print(eten[0]);
print(eten[3]) 
print(len(eten))

# 2.
boodschappen=["Melk", "Brood","Kaas"]
boodschappen.append("Appels")
boodschappen.remove("Brood")
print(boodschappen)
print(len(boodschappen))

# 3.

producten=["Koffie", "Thee", "Salade", "Hamburger"]
prijzen=[2.50, 2.00,15.00,24.00]

print(f"{producten[0]} kost {prijzen[0]:.2f}")
print(f"{producten[1]} kost {prijzen[1]:.2f}")
print(f"{producten[2]} kost {prijzen[2]:.2f}")
print(f"{producten[3]} kost {prijzen[3]:.2f}")

# met loop 

for i in range(len(producten)):
    print(f"{producten[i]} kost {prijzen[i]:.2f}")


thislist = ["apple", "strawberry", "mango", "banana", "peer"]
print(len(thislist))

thislist =["apple", "mango", "avocado", "banana", "watermeloen", "cherry"]
print(thislist[:4]) # "apple", "mango", "avocado", "banana"

thislist=["apple", "peer", "banana", "mango"]
tropical =["pineapple", "papaya", "avocado"]
thislist.extend(tropical)
print(thislist)