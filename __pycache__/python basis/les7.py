import csv

# 1.
boodschappen=["Melk", "Brood", "Kaas","Appels", "Eieren"]

with open("boodschappen.txt", "w") as bestand:
    for i in range(len(boodschappen)):
      bestand.write(f"{i+1}. {boodschappen[i]}\n")


with open("boodschappen.txt", "r") as bestand:
        print(bestand.read())

# 3.

with open("verkoop.txt", "w") as bestand:
    bestand.write("2 spijkerbroeken\n")
    bestand.write("4 jurken\n")
    bestand.write("5 jassen\n")
    
with open("verkoop.txt","a") as bestand:
    bestand.write("10 ondergoed\n")
    bestand.write("3 rokjes\n")

with open("verkoop.txt", "r") as bestand:
    print(bestand.read())

personen = [
    ["Alina", 43, "Rotterdam"],
    ["Sara", 25, "Amsterdam"],
    ["Mohamed", 35, "Utrecht"]

]

with open("personen.csv", "w", newline="") as bestand:
    schrijver = csv.writer(bestand)
    schrijver.writerow(["naam", "leeftijd", "stad"])
    for persoon in personen:
        schrijver.writerow(persoon)

with open("personen.csv","r") as bestand:
    lezer= csv.reader(bestand)
    for rij in lezer:
        print(rij)
