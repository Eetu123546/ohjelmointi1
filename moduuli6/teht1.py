import random

def noppa():
    luku = random.randint(1,6)
    return luku

luku = 0

while luku != 6:
    luku = noppa()
    print(luku)
