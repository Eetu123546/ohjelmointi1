maksimi = minimi = luku = input("Kerro luku: ")

while True:

    if luku == "":
        break

    minimi = float(minimi)
    maksimi = float(maksimi)
    luku = float(luku)

    if luku < minimi:
        minimi = luku

    elif luku > maksimi:
        maksimi = luku

    luku = input("kerro luku: ")

print(f"lopetetaan, suurin luku oli {maksimi} ja pienin oli {minimi}")
