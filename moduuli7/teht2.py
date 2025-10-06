
nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi in nimet:
        print("Nimi on jo sanottu")
    elif nimi == "":
        break
    else:
        nimet.add(nimi)

for i in nimet:
    print(i)