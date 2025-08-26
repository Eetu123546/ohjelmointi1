
pituus = float(input("Anna kuhan pituus(cm): "))

if pituus < 37:
    ero = 37 - pituus
    print(f"kuha on {ero:.2f} cm liian pieni, heitä se takaisin.")

else:
    print("Kuha on tarpeeksi suuri.")