
yritykset = 0

while True:

    kayt = input("Anna käyttäjätunnus: ")
    sala = input("Anna salasana: ")

    if kayt


    if kayt == "python" and sala == "rules":
        print("Tervetuloa!")
        break

    elif yritykset >= 5:
        print("pääsy evätty")
        break

    else:
        yritykset = yritykset + 1


