# 1.
from math import sqrt, pi, ceil, floor
import random
import datetime
import rekenmachine


print(pi)
print(sqrt(144))

print(ceil(7.3))
print(floor(7.9))

# 2.
gooien=[]

for i in range(1,6):
    gooi=random.randint(1,6)
    gooien.append(gooi)
    print(f"Gooi {i}: {gooi}")

print(f"Hoogste gooi: {max(gooien)}")


# 3.
nu = datetime.datetime.now()
print(nu.strftime("%d-%m-%Y"))
print(nu.year)

vandaag = datetime.date.today()
print(vandaag)

# 4.
print(rekenmachine.optellen(4,12))
print(rekenmachine.aftrekken(1, 8))
print(rekenmachine.vermenigvuldigen(2,9))
print(rekenmachine.delen(12,5))
