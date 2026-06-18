# 1.

def begroet(naam,tijdstip):
    if tijdstip =="ochtend":
         print(f"Goedemorgen {naam}")
    elif tijdstip =="avond":
         print(f"Goedenavond {naam}")
    else:
         print(f"Goedemiddag {naam}")

begroet("Alina", "ochtend")   
begroet("Alina", "avond")
begroet("Alina", "middag")

# 2.
def optellen(a,b):
     return a+b

print(optellen(10,5))

def aftrekken(a,b):
     return a-b

print(aftrekken(10,5))    

def vermenigvuldigen(a,b):
     return a*b

print(vermenigvuldigen(10,5))

def delen(a,b):
     return a/b

print(delen(10,5))     


# 3.
def cafe_bestelling(product,prijs,aantal):
     totaal=prijs*aantal
    
     if totaal>20:
         totaal= totaal*0.90
         return f"{aantal}x {product} = {totaal:.2f}"
     else:
          return f"{aantal}x {product} = {totaal:.2f}"

print(cafe_bestelling("Koffie", 2.50, 3))
print(cafe_bestelling("Salade", 15.00, 2))