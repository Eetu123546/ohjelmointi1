
lentokentät = {"EFHK":"Helsinki",
               "ESGG":"Göteborg Landvetter"}

def new_airport():
    icao = input("Anna ICAO koodi: ")
    nimi = input("Anna lentokentän nimi: ")
    if icao in lentokentät:
        print("tämä lentokenttä on jo listassa")
    else:
        lentokentät[icao] = nimi
        print(f"Lentokenttä {nimi} lisätty tietokantaan.")

def search_airports():
    icao = input("Anna ICAO koodi: ")
    if icao in lentokentät:
        print(f"ICAO koodi {icao} vastaa lentokenttää {lentokentät[icao]}.")
    else:
        print("Tätä lentokenttää ei ole tietokannassa")

while True:
    print("Mahdolliset komennot: search, add, exit")
    valinta = input("Anna komento: ")
    if valinta == "search":
        search_airports()
    elif valinta == "add":
        new_airport()
    elif valinta == "exit":
        print("Ohjelma sulkeutuu.")
        break
    else:
        print("Komentoa ei löydy.")

