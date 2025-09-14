import random

def noppa(max):
    luku = random.randint(1, max)
    return luku

maksimi = int(input("Anna nopan maksimiluku: "))

luku = 0

while luku != maksimi:
    luku = noppa(maksimi)
    print(luku)
