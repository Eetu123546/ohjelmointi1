import random
from classes.auto import Auto

autot = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(auto)

while True:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
    for auto in autot:
        auto.kulje(1)
    if any(auto.matka >= 10000 for auto in autot):
        break

for auto in autot:
    print(f"""
    Rekisteritunnus: {auto.rekisteritunnus}
    Huippunopeus: {auto.huippunopeus} km/h
    Nopeus: {auto.nopeus} km/h
    Matka kuljettu: {auto.matka} km""")