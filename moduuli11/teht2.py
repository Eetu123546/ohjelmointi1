from classes.auto import Sähköauto
from classes.auto import Polttomoottoriauto

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.2)

sähköauto.kiihdytä(50)
polttomoottoriauto.kiihdytä(60)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"""
Rekisteritunnus: {sähköauto.rekisteritunnus}
Huippunopeus: {sähköauto.huippunopeus} km/h
Akkukapasiteetti: {sähköauto.akkukapasiteetti} kWh
Matka kuljettu: {sähköauto.matka}""")

print(f"""
Rekisteritunnus: {polttomoottoriauto.rekisteritunnus}
Huippunopeus: {polttomoottoriauto.huippunopeus} km/h
Akkukapasiteetti: {polttomoottoriauto.tankin_koko} kWh
Matka kuljettu: {polttomoottoriauto.matka}""")
