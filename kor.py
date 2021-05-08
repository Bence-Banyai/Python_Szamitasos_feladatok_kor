import math


def kor_kerulet(r: float):
    return 2*r*math.pi


def kor_terulet(r: float):
    return math.pi*r**2


print('Kör terület és kerület számítása')
r = float(input('Adja meg a sugarat:'))
if r > 0:
    print('A kerület:', kor_kerulet(r))
    print('A terület:', kor_terulet(r))
else:
    print('Hiba: rossz adat!')
