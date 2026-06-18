def bereken_totaal(prijs,aantal):
    return float(prijs) * float(aantal)

def geef_korting(totaal,procent):
    return totaal *(1-procent/100)
    
BTWTARIEF = 0.21