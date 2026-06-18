def bereken_bestelling(prijs, aantal):
    try:
        totaal = float(prijs) * int(aantal)
        return f"Totaal: euro {totaal:.2f}"
    except ValueError:
        return "Fout: prijs en aantal moeten getallen zijn!"
    except ZeroDivisionError:
        return "Fout: aantal kan niet nul zijn!"

print(bereken_bestelling(2.50, 3))
print(bereken_bestelling("halle", 3))


def lees_bestand(bestandsnaam):
    try:
        with open(bestandsnaam, "r") as bestand:
            return bestand.read()
    except FileNotFoundError:
            return f"Bestand '{bestandsnaam}' bestaat niet!"

print(lees_bestand("boodschappen.txt"))
print(lees_bestand("bestaat_niet.txt"))


def vraag_leeftijd():
    while True:
        try:
            leeftijd= int(input("Wat is je leeftijd?"))
            if leeftijd < 0 or leeftijd > 120:
                print("Dat is geen geldige leeftijd!")
            else:
                return leeftijd
        except ValueError:
            print("Vul een getal in!")  

leeftijd = vraag_leeftijd()
print(f"Jouw leeftijd is {leeftijd}")
      

def deel(a,b):
    try:
      
        if b == 0:
           return "Je kan niet delen door nul"
        else:
           return float(a)/float(b)
    except ValueError:
        return "Vul alleen getallen in!"

print(deel(10,2))
print(deel(10,0))
print(deel("hallo", 2))


def lees_bestand(naam):
    try:
        with open(bestandnaam, "r") as bestand:
            return bestand.read()
    except FileNotFound:
        return f"Bestand {bestandnaam} bestaat niet!"    

print(lees_bestand("verkoop.txt"))  
print(lees_bestand("mybestand.txt"))  

def cafe_bestelling(product, prijs, aantal):
    try:
        totaal =float(prijs)* float(aantal)
        if aantal <=0:
            return "Aantal moet groter zijn dan 0!"
        else:
            return f"{aantal}x {product} = euro {totaal:.2f}"
    except ValueError:
        return "Prijs of Aantal moet een getal zijn!"

print(cafe_bestelling("Koffie", 2.50, 3))
print(cafe_bestelling("Thee", "duur", 2))
print(cafe_bestelling("salade", 15.00, 0))