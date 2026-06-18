class Medewerker:
    def __init__(self, naam, leeftijd, functie):
        self.naam = naam
        self.leeftijd = leeftijd
        self.functie = functie

    # Methode 1  
    def begroet(self):
        return f"Hallo, ik ben {self.naam} en ik werk als {self.functie}"

    # Methode 2
    def verjaardag(self):
        self.leeftijd += 1
        return f"{self.naam} is nu {self.leeftijd} jaar!"

    def __str__(self):
        return f"Medewerker: {self.naam} | {self.leeftijd} jaar | {self.functie}"

medewerker1 = Medewerker("Alina", 43, "Manager")
print(medewerker1.begroet())
print(medewerker1.verjaardag())

class Cafe:
    def __init__(self, naam, stad):
        self.naam=naam
        self.stad=stad
        self.menu=[]
        self.omzet=0

    def voeg_product_toe(self, product, prijs):
        self.menu.append({"product": product, "prijs": prijs})
        return f"{product} toegevoegd aan menu!"

    def toon_menu(self):
        print(f"\n Menu van {self.naam}")
        print("-" * 30)
        for item in self.menu:
            print(f"{item['product']} => euro {item['prijs']:.2f}")

    def verkoop(self, product, aantal):
        for item in self.menu:
            if item["product"] == product:
                totaal = item["prijs"] * aantal
                self.omzet += totaal
                return f"{aantal}* {product} = euro {totaal:.2f}"
        return f"{product} staat niet op het menu!"

    def toon_omzet(self):
        return f"Totale omzet: euro {self.omzet:.2f}"

    def __str__(self):
        return f"Cafe '{self.naam}' in {self.stad}"

mijn_cafe = Cafe("Cafe Alina", "Rotterdam")

print(mijn_cafe.voeg_product_toe("Koffie",2.50))
print(mijn_cafe.voeg_product_toe("Thee", 2.00))
print(mijn_cafe.voeg_product_toe("Salade", 15.00))


# Menu tonen
mijn_cafe.toon_menu()

# Verkopen
print(mijn_cafe.verkoop("Koffie",3))
print(mijn_cafe.verkoop("Salade", 2))

# Omzet tonen
print(mijn_cafe.toon_omzet())

# Object printen
print(mijn_cafe)


# Kind class -erft van Medewerker

class Manager(Medewerker):
  def __init__(self, naam, leeftijd,functie, afdeling):
     super().__init__(naam, leeftijd,functie)
     self.afdeling = afdeling

  def toon_info(self):
     return f"{self.naam} is {self.functie} van {self.afdeling}"

# Kind class

class Barista(Medewerker):
    def __init__(self, naam, leeftijd,functie, speciality):
        super().__init__(naam,leeftijd,functie)
        self.speciality = speciality

    def maak_koffie(self):
        return f"{self.naam} maak een {self.speciality}!"

manager = Manager("Alina", 23,"dokter", "chirurgie afdeling")
barista= Barista("Mike", 43,"Koffiemaker", "Cappuccino")

print(manager.begroet())
print(manager.toon_info())
print(barista.begroet())
print(barista.maak_koffie())



class Person:
    def __init__(self, naam, leeftijd, stad):
        self.naam=naam
        self.leeftijd=leeftijd
        self.stad=stad

    def begroet(self):
        return f"Hallo ik ben {self.naam} uit {self.stad}!"

    def verjaardag(self):
         self.leeftijd+=1
         return f"{self.naam} is {self.leeftijd} jaar oud!"

    def __str__(self):
        return f"'Persoon: {self.naam} | {self.leeftijd} jaar| {self.stad}'"


person1= Person("Maria", 23, "Barcelona")
person2=Person("Aryan", 10, "Rotterdam")
person3=Person("Mike", 43, "Rotterdam")

print(person1.begroet())
print(person2.verjaardag())
print(person3)


# 2.Bankrekening

class Bankrekening:
    def __init__(self, naam, saldo):
        self.naam=naam
        self.saldo=saldo

    def storten(self,bedrag):
     self.saldo += bedrag
     return f"Gestort! Nieuw saldo: euro {self.saldo:.2f}"

    def opnemen(self,bedrag):
        if bedrag > self.saldo:
           return "Niet genoeg saldo!"
        else:
            self.saldo-= bedrag
            return f"Opgenomen! Nieuw saldo: euro {self.saldo:.2f}"

    def toon_saldo(self):
        return f"Saldo van {self.naam}: euro {self.saldo:.2f}"

rekening = Bankrekening("Alina", 1000)

print(rekening.storten(500))
print(rekening.opnemen(200))
print(rekening.opnemen(2000))

# cafe class
class Cafe:
    def __init__(self, naam, stad ):
         self.naam = naam
         self.stad = stad
         self.menu=[]
         self.omzet=0

    def voeg_product_toe(self,product, prijs):
        self.menu.append({"product":product, "prijs":prijs})
        return f" {product} toegevoegd aan de menu!"

    def toon_menu(self):
        print(f"\n Menu van de {self.naam}")
        for item in self.menu:
            print(f"{item['product']} =>{item['prijs']:.2f} ")

    def verkoop(self, product, aantal):
        for item in self.menu:
            if item["product"] == product:
                totaal = item["prijs"] * aantal
                self.omzet+=totaal
                return f"{product} * {aantal} => euro {totaal:.2f}"
        return f"{product} staat niet op het menu"

cafe1 = Cafe("Alina", "Rotterdam")
cafe2 =Cafe("Mari", "Iasi")
cafe3= Cafe("Sultan", "Madrid")

print(cafe1.voeg_product_toe("Cappucino",15))
print(cafe2.toon_menu())
print(cafe3.verkoop("Americano", 10))

# a= "Hello"
# b= "World"
# print(a+b)

print(2+3*4)
print(10-5+3)

x,y,z,w="Orange", "Banana", "Cherry", "Appel"
print(x)
print(y)
print(z)

x=y=z ="Papaya"
print(x)
print(y)
print(z)

fruits =["apple", "banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

# tuple

fruits = ("apple", "banana", "cherry")

(green,yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "peer", "strawberry", "blue-berrys")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("mango", "pineapple", "guava", "papaya", "banana")
(red, *yellow, green)= fruits
print(red)
print(yellow)
print(green)

x= "Python "
y = "is "
z= "awesome"
print(x+y+z)

x= 5
y = "John"
print(x,y)

x= "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
# Sets

kleuren ={"groen", "white", "red", "yellow", "black", "red"}
print(kleuren)
kleuren.add("blue")
kleuren.remove("yellow")
print(kleuren)

b="Hello, World!"
print(b[2:])
print(b[-5:-2])

