# 1.

leeftijd=67

if leeftijd >65:
    print("U krijgt 10% senioren korting!")
else:
     print("Geen korting")

# 2.
bestelling = "koffie"
heeft_loyaliteitskaart = True

if bestelling=="koffie" and heeft_loyaliteitskaart==True:
    print("Koffie met 1 gratis koekje!")
elif bestelling=="koffie" and heeft_loyaliteitskaart==False:
    print("Koffie voor 2.50 euro")
else:
    print("Wat wilt u bestellen?")

 # 3.
cijfer=7

if cijfer>=9:
  print("Uitstekend!")
elif cijfer>=7:
  print("Goed gedaan!")
elif cijfer>=6 and cijfer<7:
  print("Voldoende")
else:
  print("Helaas,onvoldoende")
