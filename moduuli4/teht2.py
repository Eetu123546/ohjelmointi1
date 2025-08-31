tuuma = float(input("Kerro tuumat: "))

while tuuma >= 0:
    sentti = tuuma * 2.54
    print(f"{tuuma} tuumaa on {sentti} senttimetriä.")
    tuuma = float(input("Kerro tuumat: "))

print("Negatiivinen luku ohjelma sulkeutuu")