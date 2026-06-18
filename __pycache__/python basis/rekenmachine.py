def optellen(a,b):
    return a+b
def aftrekken(a,b):
    return a-b

def vermenigvuldigen(a,b):
    return a*b

def delen(a,b):
    try:
       if b==0:
         return "Je kan niet delen door nul"
       else:
         return float(a)/float(b)
    except ValueError:
        return "Vul alleen getallen in"
