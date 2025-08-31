import random

luku = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa luku: "))

    if arvaus < luku:
        print("liian pieni arvaus")

    elif arvaus > luku:
        print("liian suuri arvaus")

    elif arvaus == luku:
        print("OIKEA VASTAUS")
        break