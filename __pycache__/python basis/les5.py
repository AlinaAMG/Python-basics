# 1
boodschappen=["Melk", "Brood", "Kaas", "Appels", "Eieren"]

for i in range(len(boodschappen)):
      print(f"{i+1}. {boodschappen[i]}")

# 2
for i in range(10):
      print(f"3*{i+1} = {3*(i+1)}")


#3
producten =["Koffie", "Thee", "Salade","Hamburger"]
prijzen =[2.50,2.00, 15.00,24.00]

for i in range(len(producten)):
 if prijzen[i] >10:
      print(f"{producten[i]} kost {prijzen[i]:.2f} 🍽️  Hoofdgerecht")
 else:
      print(f"{producten[i]} kost {prijzen[i]:.2f} ☕ Drankje")