import random

heitot = int(input("Anna heittojen määrä koknaisluvulla:"))
luku = 0

for a in range(0,heitot):
    arpa = random.randint(1,6)
    luku = luku + arpa

print(luku)