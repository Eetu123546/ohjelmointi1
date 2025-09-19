
vuodenajat = "kevät", "kesä", "syksy", "talvi"

kk = int(input("Monesko kuukausi: "))

if kk <= 0:
    print("vali vali miinusluku")

elif 0 < kk < 4:
    print(f"Nyt on {vuodenajat[0]}")

elif 3 < kk < 7:
    print(f"Nyt on {vuodenajat[1]}")

elif 6 < kk < 9:
    print(f"Nyt on {vuodenajat[2]}")

elif 9 < kk < 13:
    print(f"Nyt on {vuodenajat[3]}")

else:
    print(f"{kk} ei ole kuukauden numero")