from classes.auto import Auto
from classes.kilpailu import Kilpailu
import random

autot = []
aika = 0

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while True:
    aika = aika + 1
    kilpailu.tunti_kuluu()
    if aika % 10 == 0:
        kilpailu.tulosta_tilanne()
    if kilpailu.kilpailu_ohi() == True:
        break

kilpailu.tulosta_tilanne()
