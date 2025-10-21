from classes.auto import Auto

autot = []

auto1 = Auto("ABC-123", 142)
auto2 = Auto("DEF-456", 200)
auto3 = Auto("GHJ-789", 145)

autot.append(auto3)
autot.append(auto2)
autot.append(auto1)

for auto in autot:
    print(f"""
    Rekisteritunnus: {auto.rekisteritunnus}
    Huippunopeus: {auto.huippunopeus}
    Nopeus: {auto.nopeus}
    Matka: {auto.matka}""")

